from presentation.input.user_input import UserInput
from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository
from interfaces.validator.validator import PasswordValidatorInterface, ValidatorInterface


class UserValidator(ValidatorInterface):
    def __init__(self, repository: UserRepository,
                 password_validator: PasswordValidatorInterface) -> None:
        self._repository = repository
        self._password_validator = password_validator

    def validate(self, input_user: UserInput) -> None:
        self._validate_email(input_user.email)
        self._validate_password(input_user.password)

    def _validate_email(self, email: str) -> None:
        if "@" not in email:
            raise ValueError("Invalid email")
        if self._repository.exists(Email(email)):
            raise ValueError("User already exists.")

    def _validate_password(self, password: str) -> None:
        self._password_validator.validate(password)
