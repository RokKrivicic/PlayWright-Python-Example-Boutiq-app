"""Test for successful registration"""

from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.fake_email.fake_email import FakeEmail
from page_object.registration.registration import Registration
from page_object.registration.data import valid_user


@qase.id(9)
@qase.title("Registering a new account sends the email to the new user")
def test_successful_registration(page: Page) -> None:
    """Test email sent to the new user"""
    fake_email = FakeEmail(page)
    fake_email.navigate_to_fake_email()
    initial_email = fake_email.email.inner_text()
    fake_email.modify_email()
    expect(fake_email.email).to_be_visible()
    expect(fake_email.email_input).not_to_be_visible()
    expect(fake_email.email).not_to_have_text(initial_email)
    copied_value = fake_email.email.inner_text()
    registration = Registration(page)
    registration.navigate_to_registration()
    # pylint: disable=R0801
    registration.fill_registration_form(
        copied_value,
        valid_user["password"],
        valid_user["password"],
        valid_user["date_of_birth"],
    )
    registration.accept_terms_and_condition()
    registration.button["register"].click()
    # pylint: enable = R0801
    expect(registration.notification["successful_registration"]).to_be_visible()
    fake_email.navigate_to_fake_email()
    expect(fake_email.email).to_have_text(copied_value)
    fake_email.boutiq.click()
    expect(fake_email.email_title).to_be_visible()
