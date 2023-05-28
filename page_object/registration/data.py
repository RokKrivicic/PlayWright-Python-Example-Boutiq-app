"""Test date to be used in the test files"""

valid_user = {
    "email": "Test@email.com",
    "password": "Test1234",
    "date_of_birth": "2000-02-14",
}

invalid_user = {
    "email_with_only_letters": "test",
    "empty_string": "",
    "email_without_comma": "test@",
    "email_without_letter_after_the_comma": "test@.",
    "short_password": "test",
    "password_with_only_lower_cased_letters": "testtest",
    "password_with-only_upper_cased_letters": "TESTTEST",
    "password_without_numbers": "testTest",
    "long_password": "Test123456TEST1234567",
    "invalid_date_of_birth": "2023-02-14",
}

error_message = {
    "invalid_email_address": "Invalid email address",
    "enter_an_email_address": "Enter an email address",
    "empty_password": '"password" is not allowed to be empty',
    "password_to_short": '"password" should be at least 8 characters long',
    "password_without_upper_cased_letter": '"password" should contain at least 1 upper-cased letter',
    "password_to_long": '"password" should not be longer than 20 characters',
    "password_without_lower_cased_letter": '"password" should contain at least 1 lower-cased letter',
    "password_without_number": '"password" should contain at least 1 number',
    "password_do_not_match": "Passwords do not match",
    "invalid_date": "Invalid date",
    "young_user": "You must be at least 13 years old to register",
    "terms_and_conditions_must_be_accepted": "Terms and conditions must be accepted",
}
