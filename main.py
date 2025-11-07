from uuid import UUID

from application.register_user import RegisterUserUseCase
from domain.services.user_password_validator import UserPasswordValidator
from domain.services.user_validator import UserValidator
from infrastructures.hashers.hashers import BcryptPasswordHasher
from infrastructures.persistence.user_repository import InMemoryUserRepository
from infrastructures.serializers.user_serializer import UserJsonSerializer
from interfaces.user_repository import UserRepository
from presentation.input.user_input import UserInput


def build_usecase() -> tuple[RegisterUserUseCase, InMemoryUserRepository]:
    serializer = UserJsonSerializer()
    repository = InMemoryUserRepository(serializer)
    validator = UserValidator(repository, password_validator=UserPasswordValidator())
    usecase = RegisterUserUseCase(validator=validator, repository=repository, password_hasher=BcryptPasswordHasher())
    return usecase, repository


def run_register(use_case: RegisterUserUseCase, user_repo: UserRepository, web_input: UserInput) -> UUID:
    user = use_case.execute(web_input)
    fetched = user_repo.get(user)

    assert fetched.uuid == user.uuid

    return user.uuid


if __name__ == "__main__":
    usecase, repository = build_usecase()
    data = UserInput("demo@example.com", "StrongPass1")

    user_id = run_register(usecase, repository, data)
    print(user_id)
