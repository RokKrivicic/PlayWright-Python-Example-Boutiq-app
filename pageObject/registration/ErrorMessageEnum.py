from enum import Enum


class ErrorMessage(Enum):
    InvalidEmailAddress = 'Invalid email address'
    EnterAnEmailAddress = 'Enter an email address'
    EmptyPassword = '"password" is not allowed to be empty'
    PasswordToShort = '"password" should be at least 8 characters long'
    PasswordWithoutUpperCasedLetter = '"password" should contain at least 1 upper-cased letter'
    PasswordToLong = '"password" should not be longer than 20 characters'
    PasswordWithoutLowerCasedLetter = '"password" should contain at least 1 lower-cased letter'
    PasswordWithoutNumber = '"password" should contain at least 1 number'
    PasswordDoNotMatch = 'Passwords do not match'
    InvalidDate = 'Invalid date'
    YoungUser = 'You must be at least 13 years old to register'
    TermsAndConditionsMustBeAccepted = 'Terms and conditions must be accepted'
