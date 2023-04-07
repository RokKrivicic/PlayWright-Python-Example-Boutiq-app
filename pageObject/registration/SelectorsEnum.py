from enum import Enum


class Selectors(Enum):
    EmailField = '[name="email"]'
    PasswordField = '[name="password"]'
    ConfirmPasswordField = '[name="confirmedPassword"]'
    BirthDateField = '[name="birthDate"]'
    TermsAndConditionsCheckbox = '[name="acceptedTC"]'
    RegisterButton = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > form ' \
                     '> div.sc-23ae1b82-0.jZkxht > button '
    TermsAndConditionLink = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk ' \
                            '> form > label > div > a '
    LoginLink = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > ' \
                'div.sc-9bb2e39f-0.jTCvWq > a '
    ShowPasswordButton = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > ' \
                         'form > div:nth-child(3) > img '
    ShowConfirmPasswordButton = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > ' \
                                'div.sc-89c5af6-0.gkRKCk > form > div.sc-a2612d62-1.cZXQFx.sc-23ae1b82-1.lnRuL > img '
    EmailErrorMessage = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > ' \
                        'form > div:nth-child(2) > label '
    PasswordErrorMessage = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > ' \
                           'form > div:nth-child(3) > label '
    ConfirmPasswordErrorMessage = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > ' \
                                  'div.sc-89c5af6-0.gkRKCk > form > div.sc-a2612d62-1.cZXQFx.sc-23ae1b82-1.lnRuL > ' \
                                  'label '
    DateErrorMessage = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > div.sc-89c5af6-0.gkRKCk > ' \
                       'form > div.sc-c1509d-0.jGkKKJ > label '
    TermsAndConditionErrorMessage = '#__next > div.sc-fcefa2f6-0.bMhYop > div.sc-fcefa2f6-1.btHyvh > ' \
                                    'div.sc-89c5af6-0.gkRKCk > form > label '

