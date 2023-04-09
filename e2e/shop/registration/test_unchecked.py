import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from pageObject.registration.ErrorMessageEnum import ErrorMessage
from testData.DataEnum import Data


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


def test_unchecked(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(Data.ValidEmail.value, Data.ValidPassword.value, Data.ValidPassword.value,
                                        Data.ValidDateOfBirth.value)
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.TermsAndConditionErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.TermsAndConditionErrorMessage))\
        .to_have_text(ErrorMessage.TermsAndConditionsMustBeAccepted.value)
