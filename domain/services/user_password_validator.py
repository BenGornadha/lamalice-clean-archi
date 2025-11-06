from domain.exceptions.password import PasswordTooShortError, PasswordMissingNumberError, \
    PasswordMissingSpecialCharError, PasswordMissingUppercaseError
from interfaces.validator.validator import PasswordValidatorInterface


class UserPasswordValidator(PasswordValidatorInterface):

    def __init__(self):
        self._min_length = 8
        self._require_special_char = True
        self._require_number = True
        self._require_uppercase = True

    def validate(self, password: str) -> None:
        if len(password) < self._min_length:
            raise PasswordTooShortError("Password must be at least 8 characters long.")

        if self._require_special_char and not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
            raise PasswordMissingSpecialCharError("Password must contain at least one special character.")

        if self._require_number and not any(char.isdigit() for char in password):
            raise PasswordMissingNumberError("Password must contain at least one number.")

        if self._require_uppercase and not any(char.isupper() for char in password):
            raise PasswordMissingUppercaseError("Password must contain at least one uppercase letter.")

