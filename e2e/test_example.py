import pytest
import os
from playwright.sync_api import Page, expect
from pageObject.registration.registrationPage import RegistrationPage
from pageObject.registration.registrationSelectorsEnum import RegistrationSelectors

base_url = os.environ['BASE_URL']


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


def test_example(page: Page) -> None:
    registration_page = RegistrationPage(page)
    page.goto(base_url)
    registration_page.click_element(RegistrationSelectors.RegisterButton)
    expect(registration_page.get_element(RegistrationSelectors.EmailErrorMessage)).to_be_visible()
