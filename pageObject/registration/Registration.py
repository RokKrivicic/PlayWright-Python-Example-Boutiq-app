from playwright.sync_api import Locator, Page
from pageObject.registration.SelectorsEnum import Selectors


class Registration(Page):
    def __init__(self, page: Page):
        self.page = page

    def get_element(self, locator: Selectors) -> Locator:
        return self.page.locator(locator.value)

    def click_element(self, locator: Selectors) -> None:
        self.page.locator(locator.value).nth(0).click()

    def type_into_field(self, locator: Selectors, text: str):
        self.page.locator(locator.value).nth(0).fill(text)
