"""Tests for the input field email"""

import pytest
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.invalid_combinations import INVALID_EMAIL_COMBINATIONS
from page_object.registration.data import valid_user


@qase.id(1)
@qase.title("Wrong input for email field")
@qase.ignore()
@pytest.mark.parametrize("email_value,error_message", INVALID_EMAIL_COMBINATIONS)
def test_invalid_email(page: Page, email_value, error_message) -> None:
    """Tests that validate correct error messages"""
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        email_value,
        valid_user["password"],
        valid_user["password"],
        valid_user["date_of_birth"],
    )
    registration.accept_terms_and_condition()
    registration.register_button.click()
    expect(registration.email_notification).to_be_visible()
    expect(registration.email_notification).to_have_text(error_message)
