"""Test for unchecked check box"""

from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.data import valid_user


@qase.id(5)
@qase.title("Checkbox unchecked")
def test_unchecked(page: Page) -> None:
    """Tests that validate correct error messages"""
    # pylint: disable=R0801
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        valid_user["email"],
        valid_user["password"],
        valid_user["password"],
        valid_user["date_of_birth"],
    )
    # pylint: enable=R0801
    registration.button["register"].click()
    expect(registration.notification["tac"]).to_be_visible()
    expect(registration.notification["tac"]).to_have_text(
        registration.terms_and_conditions_error_message
    )
