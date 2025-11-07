from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from uuid import UUID

from application.register_user import RegisterUserUseCase
from domain.entities.user import UserRegistered
from presentation.input.user_input import UserInput
from domain.services.user_password_validator import UserPasswordValidator
from domain.services.user_validator import UserValidator
from infrastructures.hashers.hashers import BcryptPasswordHasher
from infrastructures.persistence.user_repository import InMemoryUserRepository
from infrastructures.serializers.user_serializer import UserJsonSerializer
from interfaces.user_repository import UserRepository


class Container(containers.DeclarativeContainer):

    serializer = providers.Singleton(
        UserJsonSerializer
    )

    repository = providers.Singleton(
        InMemoryUserRepository,
        user_serializer=serializer
    )

    password_validator = providers.Singleton(UserPasswordValidator,
    )

    validator = providers.Singleton(
        UserValidator,
        repository=repository,
        password_validator=password_validator
    )

    password_hasher = providers.Singleton(
        BcryptPasswordHasher
    )

    register_user_usecase = providers.Singleton(
        RegisterUserUseCase,
        validator=validator,
        repository=repository,
        password_hasher=password_hasher
    )


@inject
def run_register(
    web_input: UserInput,
    use_case: RegisterUserUseCase = Provide[Container.register_user_usecase],
    user_repo: UserRepository = Provide[Container.repository]
) -> UserRegistered:
    user = use_case.execute(input=web_input)
    fetched = user_repo.get(user)
    assert fetched.uuid == user.uuid
    return user


def main() -> None:
    # Création et configuration du conteneur
    container = Container()
    container.wire(modules=[__name__])

    # Création des données d'entrée
    data = UserInput("demo@example.com", "Strong@Pass1")

    # Exécution du cas d'utilisation
    user = run_register(data)
    print(f"Utilisateur créé avec l'UUID: {user.uuid}")
    print(f"Utilisateur créé avec l'email: {user.email}")
    print(f"Utilisateur créé avec le password: {user.password_hash}")
    print(f"Utilisateur créé à: {user.registered_at}")

if __name__ == "__main__":
    main()