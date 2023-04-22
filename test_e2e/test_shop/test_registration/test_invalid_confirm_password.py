import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.invalid_combinations import INVALID_CONFIRM_PASSWORD_COMBINATIONS
from pageObject.registration.data import valid_user
from qaseio.pytest import qase


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(3)
@qase.title("Wrong input for field confirm password")
@qase.ignore()
@pytest.mark.parametrize("confirm_password_value,error_message", INVALID_CONFIRM_PASSWORD_COMBINATIONS)
def test_invalid_confirm_password(page: Page, confirm_password_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(valid_user['email'], valid_user['password'], confirm_password_value,
                                        valid_user['date_of_birth'])
    registration.accept_terms_and_condition()
    registration.register_button.click()
    expect(registration.conf_pass_notification).to_be_visible()
    expect(registration.conf_pass_notification).to_have_text(error_message)
