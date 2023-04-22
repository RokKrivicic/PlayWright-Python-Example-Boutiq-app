import pytest
from playwright.sync_api import Page, expect
from pageObject.registration.Registration import Registration
from qaseio.pytest import qase
from pageObject.registration.data import invalid_user, error_message


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


@qase.id(6)
@qase.title("All inputs wrongly inserted")
def test_all_invalid_inputs(page: Page) -> None:
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(invalid_user['email_with_only_letters'],
                                        invalid_user['short_password'],
                                        invalid_user['password_with-only_upper_cased_letters'],
                                        invalid_user['invalid_date_of_birth'])
    registration.register_button.click()
    expect(registration.email_notification).to_be_visible()
    expect(registration.password_notification).to_be_visible()
    expect(registration.conf_pass_notification).to_be_visible()
    expect(registration.date_notification).to_be_visible()
    expect(registration.tac_notifications).to_be_visible()
    expect(registration.email_notification).to_have_text(error_message['invalid_email_address'])
    expect(registration.password_notification).to_have_text(error_message['password_to_short'])
    expect(registration.conf_pass_notification).to_have_text(error_message['password_do_not_match'])
    expect(registration.date_notification).to_have_text(error_message['young_user'])
    expect(registration.tac_notifications).to_have_text(error_message['terms_and_conditions_must_be_accepted'])
