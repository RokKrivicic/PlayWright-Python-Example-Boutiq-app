"""Tests for the input field date of birth"""

import pytest
from qaseio.pytest import qase
from playwright.sync_api import Page, expect
from page_object.registration.registration import Registration
from page_object.registration.invalid_combinations import INVALID_DATE_COMBINATIONS
from page_object.registration.data import valid_user


@qase.id(4)
@qase.title("Wrong input for field date of birth")
@qase.ignore()
@pytest.mark.parametrize("date_of_birth_value,error_message", INVALID_DATE_COMBINATIONS)
def test_invalid_date_of_birth(page: Page, date_of_birth_value, error_message) -> None:
    """Tests that validate correct error messages"""
    # pylint: disable=R0801
    registration = Registration(page)
    registration.navigate_to_registration()
    registration.fill_registration_form(
        valid_user["email"],
        valid_user["password"],
        valid_user["password"],
        date_of_birth_value,
    )
    # pylint: enable=R0801
    registration.accept_terms_and_condition()
    registration.register_button.click()
    expect(registration.date_notification).to_be_visible()
    expect(registration.date_notification).to_have_text(error_message)
