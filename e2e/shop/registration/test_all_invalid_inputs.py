import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from pageObject.registration.WrongInputValuesEnum import WrongInputValues
from pageObject.registration.ErrorMessageEnum import ErrorMessage
from qaseio.pytest import qase


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(6)
@qase.title("All inputs wrongly inserted")
def test_all_invalid_inputs(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(WrongInputValues.EmailWithOnlyLetters.value,
                                        WrongInputValues.ShortPassword.value,
                                        WrongInputValues.PasswordWithOnlyUpperCasedLetters.value,
                                        WrongInputValues.InvalidDateOfBirth.value)
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.EmailErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.PasswordErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.ConfirmPasswordErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.DateErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.TermsAndConditionErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.EmailErrorMessage)).to_have_text(ErrorMessage.InvalidEmailAddress.value)
    expect(registration.get_element(Selectors.PasswordErrorMessage)).to_have_text(ErrorMessage.PasswordToShort.value)
    expect(registration.get_element(Selectors.ConfirmPasswordErrorMessage))\
        .to_have_text(ErrorMessage.PasswordDoNotMatch.value)
    expect(registration.get_element(Selectors.DateErrorMessage)).to_have_text(ErrorMessage.YoungUser.value)
    expect(registration.get_element(Selectors.TermsAndConditionErrorMessage))\
        .to_have_text(ErrorMessage.TermsAndConditionsMustBeAccepted.value)
