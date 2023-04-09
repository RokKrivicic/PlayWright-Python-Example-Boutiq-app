import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from testData.registration.invalid_combinations import INVALID_CONFIRM_PASSWORD_COMBINATIONS
from testData.DataEnum import Data


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@pytest.mark.parametrize("confirm_password_value,error_message", INVALID_CONFIRM_PASSWORD_COMBINATIONS)
def test_invalid_confirm_password(page: Page, confirm_password_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(Data.ValidEmail.value, Data.ValidPassword.value, confirm_password_value,
                                        Data.ValidDateOfBirth.value)
    registration.accept_terms_and_condition()
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.ConfirmPasswordErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.ConfirmPasswordErrorMessage)).to_have_text(error_message)
