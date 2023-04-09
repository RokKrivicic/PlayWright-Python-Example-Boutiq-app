import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from testData.registration.invalid_combinations import INVALID_EMAIL_COMBINATIONS
from testData.DataEnum import Data


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@pytest.mark.parametrize("email_value,error_message", INVALID_EMAIL_COMBINATIONS)
def test_invalid_email(page: Page, email_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(email_value, Data.ValidPassword.value, Data.ValidPassword.value,
                                        Data.ValidDateOfBirth.value)
    registration.accept_terms_and_condition()
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.EmailErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.EmailErrorMessage)).to_have_text(error_message)
