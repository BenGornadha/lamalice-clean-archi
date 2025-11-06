

class PassWordException(Exception):
    """Base exception for password-related errors."""
    pass

class PasswordTooShortError(PassWordException):
    """Exception raised for weak passwords."""
    def __init__(self, message: str = "The provided password is too short.") -> None:
        super().__init__(message)

class PasswordMissingNumberError(PassWordException):
    """Exception raised when password is missing a number."""
    def __init__(self, message: str = "The password must contain at least one number.") -> None:
        super().__init__(message)

class PasswordMissingSpecialCharError(PassWordException):
    """Exception raised when password is missing a special character."""
    def __init__(self, message: str = "The password must contain at least one special character.") -> None:
        super().__init__(message)

class PasswordMissingUppercaseError(PassWordException):
    """Exception raised when password is missing an uppercase letter."""
    def __init__(self, message: str = "The password must contain at least one uppercase letter.") -> None:
        super().__init__(message)
