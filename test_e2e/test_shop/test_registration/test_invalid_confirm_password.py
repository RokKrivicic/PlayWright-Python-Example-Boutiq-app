"""Tests for the input field confirm password"""

import pytest
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.invalid_combinations import (
    INVALID_CONFIRM_PASSWORD_COMBINATIONS,
)
from page_object.registration.data import valid_user


@qase.id(3)
@qase.title("Wrong input for field confirm password")
@qase.ignore()
@pytest.mark.parametrize(
    "confirm_password_value,error_message", INVALID_CONFIRM_PASSWORD_COMBINATIONS
)
def test_invalid_confirm_password(
    page: Page, confirm_password_value, error_message
) -> None:
    """Tests that validate correct error messages"""
    # pylint: disable=R0801
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        valid_user["email"],
        valid_user["password"],
        confirm_password_value,
        valid_user["date_of_birth"],
    )
    # pylint: enable = R0801
    registration.accept_terms_and_condition()
    registration.button["register"].click()
    expect(registration.notification["confirm_password"]).to_be_visible()
    expect(registration.notification["confirm_password"]).to_have_text(error_message)
