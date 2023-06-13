"""Page object for fake email page"""

from playwright.sync_api import Optional, Response
from utils.create_unique_email import current_time_string, new_string

EMAIL_URL = "https://www.fakemail.net"


class FakeEmail:
    """FakeEmail page locators and methods"""

    def __init__(self, page):
        self.page = page

        self.edit_button = page.get_by_role("link", name="Edit")

        self.email_input = page.locator('input[name="emailInput"]')

        self.confirm_button = page.get_by_text("Confirm")

        self.email = page.locator("#email")

        self.boutiq = page.get_by_role("cell", name="Welcome to Boutiq!")
        self.email_title = page.frame_locator("#iframeMail").get_by_role(
            "heading", name="Welcome to Boutiq!"
        )

    def navigate_to_fake_email(self) -> Optional[Response]:
        """Method that opens the defined url"""
        return self.page.goto(EMAIL_URL)

    def modify_email(self) -> None:
        """Method that modifies the current email"""
        self.edit_button.click()
        self.email_input.click()
        self.email_input.type(current_time_string)
        self.email_input.click()
        self.email_input.type(new_string)
        self.confirm_button.click()
