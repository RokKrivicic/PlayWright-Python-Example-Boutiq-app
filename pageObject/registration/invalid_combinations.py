from pageObject.registration.data import invalid_user, error_message

INVALID_EMAIL_COMBINATIONS = [
    (invalid_user['empty_string'], error_message['enter_an_email_address']),
    (invalid_user['email_with_only_letters'], error_message['invalid_email_address']),
    (invalid_user['email_without_comma'], error_message['invalid_email_address']),
    (invalid_user['email_without_letter_after_the_comma'], error_message['invalid_email_address'])
]

INVALID_PASSWORD_COMBINATIONS = [
    (invalid_user['empty_string'], error_message['empty_password']),
    (invalid_user['short_password'], error_message['password_to_short']),
    (invalid_user['password_with_only_lower_cased_letters'], error_message['password_without_upper_cased_letter']),
    (invalid_user['password_with-only_upper_cased_letters'], error_message['password_without_lower_cased_letter']),
    (invalid_user['password_without_numbers'], error_message['password_without_number']),
    (invalid_user['long_password'], error_message['password_to_long'])
]

INVALID_CONFIRM_PASSWORD_COMBINATIONS = [
    (invalid_user['empty_string'], error_message['password_do_not_match']),
    (invalid_user['short_password'], error_message['password_do_not_match']),
    (invalid_user['password_with_only_lower_cased_letters'], error_message['password_do_not_match']),
    (invalid_user['password_with-only_upper_cased_letters'], error_message['password_do_not_match']),
    (invalid_user['password_without_numbers'], error_message['password_do_not_match']),
    (invalid_user['long_password'], error_message['password_do_not_match'])
]

INVALID_DATE_COMBINATIONS = [
    (invalid_user['empty_string'], error_message['invalid_date']),
    (invalid_user['invalid_date_of_birth'], error_message['young_user'])
]
