from playwright.sync_api import Locator, Page
from pageObject.registration.registrationSelectorsEnum import RegistrationSelectors


class RegistrationPage(Page):
    def __init__(self, page: Page):
        self.page = page

    def get_element(self, locator: RegistrationSelectors) -> Locator:
        return self.page.locator(locator.value)

    def click_element(self, locator: RegistrationSelectors) -> None:
        self.page.locator(locator.value).click()
