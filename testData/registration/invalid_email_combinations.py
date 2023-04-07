from pageObject.registration.WrongInputValuesEnum import WrongInputValues
from pageObject.registration.ErrorMessageEnum import ErrorMessage

INVALID_EMAIL_COMBINATIONS = [
    (WrongInputValues.EmptyString.value, ErrorMessage.EnterAnEmailAddress.value),
    (WrongInputValues.EmailWithOnlyLetters.value, ErrorMessage.InvalidEmailAddress.value),
    (WrongInputValues.EmailWithoutComma.value, ErrorMessage.InvalidEmailAddress.value),
    (WrongInputValues.EmailWithoutLetterAfterTheComma.value, ErrorMessage.InvalidEmailAddress.value)
]
