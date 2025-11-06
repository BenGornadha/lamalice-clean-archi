

class PassWordException(Exception):
    pass

class PasswordTooShortError(PassWordException):
    def __init__(self, message: str = "The provided password is too short.") -> None:
        super().__init__(message)

class PasswordMissingNumberError(PassWordException):
    def __init__(self, message: str = "The password must contain at least one number.") -> None:
        super().__init__(message)

class PasswordMissingSpecialCharError(PassWordException):
    def __init__(self, message: str = "The password must contain at least one special character.") -> None:
        super().__init__(message)

class PasswordMissingUppercaseError(PassWordException):
    def __init__(self, message: str = "The password must contain at least one uppercase letter.") -> None:
        super().__init__(message)
