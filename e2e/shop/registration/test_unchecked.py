from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.data import valid_user
from qaseio.pytest import qase
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(5)
@qase.title("Checkbox unchecked")
def test_unchecked(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(valid_user['email'], valid_user['password'], valid_user['password'],
                                        valid_user['date_of_birth'])
    registration.register_button.click()
    expect(registration.tac_notifications).to_be_visible()
    expect(registration.tac_notifications).to_have_text(registration.terms_and_conditions_error_message)
