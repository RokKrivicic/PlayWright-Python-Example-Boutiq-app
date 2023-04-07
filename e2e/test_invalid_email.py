import pytest
import os
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from testData.registration.invalid_email_combinations import INVALID_EMAIL_COMBINATIONS

base_url = os.environ['BASE_URL']


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@pytest.mark.parametrize("email_value,error_message", INVALID_EMAIL_COMBINATIONS)
def test_example(page: Page, email_value, error_message) -> None:
    registration_page = Registration(page)
    page.goto(base_url)
    registration_page.click_element(Selectors.EmailField)
    registration_page.type_into_field(Selectors.EmailField, email_value)
    registration_page.type_into_field(Selectors.PasswordField, 'Test1234$')
    registration_page.type_into_field(Selectors.ConfirmPasswordField, 'Test1234$')
    registration_page.click_element(Selectors.RegisterButton)
    expect(registration_page.get_element(Selectors.EmailErrorMessage)).to_be_visible()
    expect(registration_page.get_element(Selectors.EmailErrorMessage)).to_have_text(error_message)
