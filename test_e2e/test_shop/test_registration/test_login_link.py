"""Test for the login link"""

import re
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration


@qase.id(7)
@qase.title("Login link redirects to Login page")
def test_login_link(page: Page) -> None:
    """Test redirection of the login link"""
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.login_link.click()
    expect(page).to_have_url(re.compile(".*login"))
