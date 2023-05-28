"""Page object for registration page"""

import os
from playwright.sync_api import Optional, Response

base_url = os.environ["BASE_URL"] + "/register"


class Registration:
    """Registration page locators and methods"""

    def __init__(self, page):
        self.page = page

        self.registration_field = {
            "email": page.locator('[name="email"]').nth(0),
            "password": page.locator('[name="password"]').nth(0),
            "confirm_password": page.locator('[name="confirmedPassword"]').nth(0),
            "birth_date": page.locator('[name="birthDate"]').nth(0),
        }

        self.terms_and_conditions_checkbox = page.get_by_role(
            "checkbox", name="I agree to the terms and conditions"
        )

        self.button = {
            "register": page.get_by_role("button", name="Register"),
            "show_password": page.locator(
                ".sc-a9b05490-1 > form > div:nth-child(3) > .sc-a2612d62-5"
            ),
            "show_confirm_password": page.locator(
                ".sc-a9b05490-1 > form > div:nth-child(4) > .sc-a2612d62-5"
            ),
        }

        self.link = {
            "terms_and_conditions": page.get_by_role(
                "link", name="terms and conditions"
            ),
            "login": page.get_by_text("Login here").nth(0),
        }

        self.notification = {
            "email": page.locator("form > div:nth-child(2) > label").nth(0),
            "password": page.locator("form > div:nth-child(3) > label").nth(0),
            "confirm_password": page.locator(
                "form > div.sc-a2612d62-1.cZXQFx.sc-23ae1b82-1.lnRuL > label"
            ).nth(0),
            "date": page.locator("form > div.sc-c1509d-0.jGkKKJ > label").nth(0),
            "tac": page.locator("form > label").nth(0),
        }

        self.terms_and_conditions_error_message = (
            "Terms and conditions must be accepted"
        )

    def navigate_to_registration(self) -> Optional[Response]:
        """Method that opens the defined url"""

        return self.page.goto(base_url)

    def fill_registration_form(
        self, email: str, password: str, confirm_password: str, birth_date: str
    ) -> None:
        """Method that fills the registration form with the provided parameters"""

        self.registration_field["email"].fill(email)
        self.registration_field["password"].fill(password)
        self.registration_field["confirm_password"].fill(confirm_password)
        self.registration_field["birth_date"].fill(birth_date)

    def accept_terms_and_condition(self) -> None:
        """Method that checks the TAC checkbox"""

        self.terms_and_conditions_checkbox.check()
