"""Tests for the input field password"""

import pytest
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.invalid_combinations import INVALID_PASSWORD_COMBINATIONS
from page_object.registration.data import valid_user


@qase.id(2)
@qase.title("Wrong input for field password")
@qase.ignore()
@pytest.mark.parametrize("password_value,error_message", INVALID_PASSWORD_COMBINATIONS)
def test_invalid_password(page: Page, password_value, error_message) -> None:
    """Tests that validate correct error messages"""
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        valid_user["email"],
        password_value,
        valid_user["password"],
        valid_user["date_of_birth"],
    )
    registration.accept_terms_and_condition()
    registration.button["register"].click()
    expect(registration.notification["password"]).to_be_visible()
    expect(registration.notification["password"]).to_have_text(error_message)
