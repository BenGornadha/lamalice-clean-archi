from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository


class UserValidator:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def validate(self, email: str) -> None:
        if "@" not in email:
            raise ValueError("Invalid email")
        if self._repository.exists(Email(email)):
            raise ValueError("User already exists.")
