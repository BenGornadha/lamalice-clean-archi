import datetime
from uuid import uuid4

from domain.entities.user import UserRegistered, UserInput
from domain.services.user_validator import UserValidator
from domain.value_objects.email import Email
from interfaces.password_hasher import PasswordHasherInterface
from interfaces.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(self, validator: UserValidator,
                 password_hasher: PasswordHasherInterface,
                 repository: UserRepository) -> None:
        self._validator = validator
        self._repo = repository
        self._password_hasher = password_hasher

    def execute(self, input: UserInput) -> UserRegistered:
        self._validator.validate(input_user=input)
        password_hashed = self._password_hasher.hash(input.password)

        user = UserRegistered(uuid=uuid4(), email=Email(input.email), password_hash=password_hashed,
                              registered_at=datetime.datetime.now())
        self._repo.save(user)

        return user
