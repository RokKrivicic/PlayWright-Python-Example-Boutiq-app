import pytest
import re
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from qaseio.pytest import qase


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(8)
@qase.title("Terms and condition link redirects to Terms and condition page")
def test_terms_and_conditions_link(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    with page.expect_popup() as tab:
        registration.terms_and_conditions_link.click()
    new_page = tab.value
    expect(new_page).to_have_url(re.compile('.*terms-conditions'))


