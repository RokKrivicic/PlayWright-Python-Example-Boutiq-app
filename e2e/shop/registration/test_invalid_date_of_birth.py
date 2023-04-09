import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from testData.registration.invalid_combinations import INVALID_DATE_COMBINATIONS
from testData.DataEnum import Data


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@pytest.mark.parametrize("date_of_birth_value,error_message", INVALID_DATE_COMBINATIONS)
def test_invalid_date_of_birth(page: Page, date_of_birth_value, error_message) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(Data.ValidEmail.value, Data.ValidPassword.value, Data.ValidPassword.value,
                                        date_of_birth_value)
    registration.accept_terms_and_condition()
    registration.click_element(Selectors.RegisterButton)
    expect(registration.get_element(Selectors.DateErrorMessage)).to_be_visible()
    expect(registration.get_element(Selectors.DateErrorMessage)).to_have_text(error_message)
