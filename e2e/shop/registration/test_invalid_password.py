import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from testData.registration.invalid_combinations import INVALID_PASSWORD_COMBINATIONS
from testData.DataEnum import Data


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@pytest.mark.parametrize("password_value,error_message", INVALID_PASSWORD_COMBINATIONS)
def test_invalid_password(page: Page, password_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(Data.ValidEmail.value, password_value, Data.ValidPassword.value,
                                        Data.ValidDateOfBirth.value)
    registration.accept_terms_and_condition()
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.PasswordErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.PasswordErrorMessage)).to_have_text(error_message)
