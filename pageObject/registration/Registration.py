import os
from playwright.sync_api import Locator, Page, Optional, Response
from pageObject.registration.SelectorsEnum import Selectors

base_url = os.environ['BASE_URL']


class Registration(Page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def navigate_to_registration(self) -> Optional[Response]:
        return self.page.goto(base_url)

    def get_element(self, locator: Selectors) -> Locator:
        return self.page.locator(locator.value).nth(0)

    def click_element(self, locator: Selectors) -> None:
        self.page.locator(locator.value).nth(0).click()

    def type_into_field(self, locator: Selectors, text: str) -> None:
        self.click_element(locator)
        self.page.locator(locator.value).nth(0).fill(text)

    def fill_registration_form(self, email: str, password: str, confirm_password: str, birth_date: str) -> None:
        self.type_into_field(Selectors.EmailField, email)
        self.type_into_field(Selectors.PasswordField, password)
        self.type_into_field(Selectors.ConfirmPasswordField, confirm_password)
        self.type_into_field(Selectors.BirthDateField, birth_date)

    def accept_terms_and_condition(self) -> None:
        self.get_element(Selectors.TermsAndConditionsCheckbox).check()
