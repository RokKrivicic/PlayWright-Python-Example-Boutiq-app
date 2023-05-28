"""Test for the Terms and condition link"""

import re
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration


@qase.id(8)
@qase.title("Terms and condition link redirects to Terms and condition page")
def test_terms_and_conditions_link(page: Page) -> None:
    """Test redirection of the Terms and condition link"""
    registration = Registration(page)
    registration.navigate_to_registration()
    with page.expect_popup() as tab:
        registration.link["terms_and_conditions"].click()
    new_page = tab.value
    expect(new_page).to_have_url(re.compile(".*terms-conditions"))
