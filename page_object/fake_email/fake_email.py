"""Page object for fake email page"""

from playwright.sync_api import Optional, Response

EMAIL_URL = "https://www.fakemail.net"
EMAIL_NAME = "Welcome to Boutiq!"
TEST_STRING = "test"


class FakeEmail:
    """FakeEmail page locators and methods"""

    def __init__(self, page):
        self.page = page

        self.edit_button = page.get_by_role("link", name="Edit")

        self.email_input = page.locator('input[name="emailInput"]')

        self.confirm_button = page.get_by_text("Confirm")

        self.email = page.locator("#email")

        self.email_cell_name = page.get_by_role("cell", name=EMAIL_NAME)

        self.email_title = page.frame_locator("#iframeMail").get_by_role(
            "heading", name=EMAIL_NAME
        )

    def navigate_to(self) -> Optional[Response]:
        """Method that opens the defined url"""
        return self.page.goto(EMAIL_URL)

    def modify_email(self) -> None:
        """Method that modifies the current email"""
        self.edit_button.click()
        self.email_input.click()
        self.email_input.type(TEST_STRING)
        self.email_input.click()
        self.email_input.type(TEST_STRING)
        self.confirm_button.click()
