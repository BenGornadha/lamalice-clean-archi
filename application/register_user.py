import datetime
from uuid import uuid4

from application.dto.website_input import RegisterUserInput
from domain.entities.user import User
from domain.services.user_validator import UserValidator
from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(self, validator: UserValidator, repository: UserRepository) -> None:
        self._validator = validator
        self._repo = repository

    def execute(self, input: RegisterUserInput) -> User:
        self._validator.validate(input.email)
        user = User(uuid=uuid4(), email=Email(input.email), registered_at=datetime.datetime.now())
        self._repo.save(user)
        return user
