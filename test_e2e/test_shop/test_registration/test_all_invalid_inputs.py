"""Test for the input fields error"""

from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.data import invalid_user, error_message


@qase.id(6)
@qase.title("All inputs wrongly inserted")
def test_all_invalid_inputs(page: Page) -> None:
    """Test invalid inputs error messages"""
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        invalid_user["email_with_only_letters"],
        invalid_user["short_password"],
        invalid_user["password_with-only_upper_cased_letters"],
        invalid_user["invalid_date_of_birth"],
    )
    registration.button["register"].click()
    expect(registration.notification["email"]).to_be_visible()
    expect(registration.notification["password"]).to_be_visible()
    expect(registration.notification["confirm_password"]).to_be_visible()
    expect(registration.notification["date"]).to_be_visible()
    expect(registration.notification["tac"]).to_be_visible()
    expect(registration.notification["email"]).to_have_text(
        error_message["invalid_email_address"]
    )
    expect(registration.notification["password"]).to_have_text(
        error_message["password_to_short"]
    )
    expect(registration.notification["confirm_password"]).to_have_text(
        error_message["password_do_not_match"]
    )
    expect(registration.notification["date"]).to_have_text(error_message["young_user"])
    expect(registration.notification["tac"]).to_have_text(
        error_message["terms_and_conditions_must_be_accepted"]
    )
