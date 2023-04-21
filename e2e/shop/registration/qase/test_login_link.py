import pytest
import re
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from pageObject.registration.SelectorsEnum import Selectors
from qaseio.pytest import qase


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(7)
@qase.title("Login link redirects to Login page")
def test_login_link(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.click_element(Selectors.LoginLink)
    expect(page).to_have_url(re.compile('.*login'))

