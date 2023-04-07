from enum import Enum


class WrongInputValues(Enum):
    EmailWithOnlyLetters = 'test'
    EmptyString = ''
    EmailWithoutComma = 'test@'
    EmailWithoutLetterAfterTheComma = 'test@.'
