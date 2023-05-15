"""Page object for registration page"""

import os
from playwright.sync_api import Optional, Response

base_url = os.environ["BASE_URL"] + "/register"


class Registration:
    """Registration page locators and methods"""

    def __init__(self, page):
        self.page = page
        self.registration_fields = {
            self.email_field: page.locator('[name="email"]'),
            self.password_field : page.locator('[name="password"]'),
            self.confirm_password_field : page.locator('[name="confirmedPassword"]')
        }
        #self.email_field = page.locator('[name="email"]')
        #self.password_field = page.locator('[name="password"]')
        #self.confirm_password_field = page.locator('[name="confirmedPassword"]')
        self.birth_date_field = page.locator('[name="birthDate"]')
        self.terms_and_conditions_checkbox = page.get_by_role(
            "checkbox", name="I agree to the terms and conditions"
        )
        self.register_button = page.get_by_role("button", name="Register")
        self.terms_and_conditions_link = page.get_by_role(
            "link", name="terms and conditions"
        )
        self.login_link = page.get_by_text("Login here").nth(0)
        self.show_password_button = page.locator(
            ".sc-a9b05490-1 > form > div:nth-child(3) > .sc-a2612d62-5"
        )
        self.show_confirm_password_button = page.locator(
            ".sc-a9b05490-1 > form > div:nth-child(4) > .sc-a2612d62-5"
        )
        self.email_notification = page.locator("form > div:nth-child(2) > label").nth(0)
        self.password_notification = page.locator(
            "form > div:nth-child(3) > label"
        ).nth(0)
        self.conf_pass_notification = page.locator(
            "form > div.sc-a2612d62-1.cZXQFx.sc-23ae1b82-1.lnRuL > label"
        ).nth(0)
        self.date_notification = page.locator(
            "form > div.sc-c1509d-0.jGkKKJ > label"
        ).nth(0)
        self.tac_notifications = page.locator("form > label").nth(0)
        self.terms_and_conditions_error_message = (
            "Terms and conditions must be accepted"
        )

    def navigate_to_registration(self) -> Optional[Response]:
        return self.page.goto(base_url)

    def fill_registration_form(
        self, email: str, password: str, confirm_password: str, birth_date: str
    ) -> None:
        self.email_field.nth(0).fill(email)
        self.password_field.nth(0).fill(password)
        self.confirm_password_field.nth(0).fill(confirm_password)
        self.birth_date_field.nth(0).fill(birth_date)

    def accept_terms_and_condition(self) -> None:
        self.terms_and_conditions_checkbox.check()
