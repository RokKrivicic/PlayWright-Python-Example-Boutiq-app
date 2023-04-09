from enum import Enum


class WrongInputValues(Enum):
    EmailWithOnlyLetters = 'test'
    EmptyString = ''
    EmailWithoutComma = 'test@'
    EmailWithoutLetterAfterTheComma = 'test@.'
    ShortPassword = 'test'
    PasswordWithOnlyLowerCasedLetters = 'testtest'
    PasswordWithOnlyUpperCasedLetters = 'TESTTEST'
    PasswordWithoutNumbers = 'testTest'
    LongPassword = 'Test123456TEST1234567'
    InvalidDateOfBirth = '2023-02-14'
