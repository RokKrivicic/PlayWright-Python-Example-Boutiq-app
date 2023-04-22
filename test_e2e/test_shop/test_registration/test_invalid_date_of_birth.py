import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.invalid_combinations import INVALID_DATE_COMBINATIONS
from pageObject.registration.data import valid_user
from qaseio.pytest import qase


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(4)
@qase.title("Wrong input for field date of birth")
@qase.ignore()
@pytest.mark.parametrize("date_of_birth_value,error_message", INVALID_DATE_COMBINATIONS)
def test_invalid_date_of_birth(page: Page, date_of_birth_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(valid_user['email'], valid_user['password'], valid_user['password'],
                                        date_of_birth_value)
    registration.accept_terms_and_condition()
    registration.register_button.click()
    expect(registration.date_notification).to_be_visible()
    expect(registration.date_notification).to_have_text(error_message)
