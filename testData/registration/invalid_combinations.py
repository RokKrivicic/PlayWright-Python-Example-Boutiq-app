from pageObject.registration.WrongInputValuesEnum import WrongInputValues
from pageObject.registration.ErrorMessageEnum import ErrorMessage

INVALID_EMAIL_COMBINATIONS = [
    (WrongInputValues.EmptyString.value, ErrorMessage.EnterAnEmailAddress.value),
    (WrongInputValues.EmailWithOnlyLetters.value, ErrorMessage.InvalidEmailAddress.value),
    (WrongInputValues.EmailWithoutComma.value, ErrorMessage.InvalidEmailAddress.value),
    (WrongInputValues.EmailWithoutLetterAfterTheComma.value, ErrorMessage.InvalidEmailAddress.value)
]

INVALID_PASSWORD_COMBINATIONS = [
    (WrongInputValues.EmptyString.value, ErrorMessage.EmptyPassword.value),
    (WrongInputValues.ShortPassword.value, ErrorMessage.PasswordToShort.value),
    (WrongInputValues.PasswordWithOnlyLowerCasedLetters.value, ErrorMessage.PasswordWithoutUpperCasedLetter.value),
    (WrongInputValues.PasswordWithOnlyUpperCasedLetters.value, ErrorMessage.PasswordWithoutLowerCasedLetter.value),
    (WrongInputValues.PasswordWithoutNumbers.value, ErrorMessage.PasswordWithoutNumber.value),
    (WrongInputValues.LongPassword.value, ErrorMessage.PasswordToLong.value)
]

INVALID_CONFIRM_PASSWORD_COMBINATIONS = [
    (WrongInputValues.EmptyString.value, ErrorMessage.PasswordDoNotMatch.value),
    (WrongInputValues.ShortPassword.value, ErrorMessage.PasswordDoNotMatch.value),
    (WrongInputValues.PasswordWithOnlyLowerCasedLetters.value, ErrorMessage.PasswordDoNotMatch.value),
    (WrongInputValues.PasswordWithOnlyUpperCasedLetters.value, ErrorMessage.PasswordDoNotMatch.value),
    (WrongInputValues.PasswordWithoutNumbers.value, ErrorMessage.PasswordDoNotMatch.value),
    (WrongInputValues.LongPassword.value, ErrorMessage.PasswordDoNotMatch.value)
]

INVALID_DATE_COMBINATIONS = [
    (WrongInputValues.EmptyString.value, ErrorMessage.InvalidDate.value),
    (WrongInputValues.InvalidDateOfBirth.value, ErrorMessage.YoungUser.value)
]
