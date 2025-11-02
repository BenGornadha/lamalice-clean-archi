from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from uuid import UUID

from application.dto.website_input import RegisterUserInput
from application.register_user import RegisterUserUseCase
from domain.services.user_validator import UserValidator
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

    validator = providers.Singleton(
        UserValidator,
        repository=repository
    )

    register_user_usecase = providers.Singleton(
        RegisterUserUseCase,
        validator=validator,
        repository=repository
    )


@inject
def run_register(
    web_input: RegisterUserInput,
    use_case: RegisterUserUseCase = Provide[Container.register_user_usecase],
    user_repo: UserRepository = Provide[Container.repository]
) -> UUID:
    user = use_case.execute(web_input)
    fetched = user_repo.get(user)
    assert fetched.uuid == user.uuid
    return user.uuid


def main() -> None:
    # Création et configuration du conteneur
    container = Container()
    container.wire(modules=[__name__])

    # Création des données d'entrée
    data = RegisterUserInput("demo@example.com", "StrongPass1")

    # Exécution du cas d'utilisation
    user_id = run_register(data)
    print(f"Utilisateur créé avec l'UUID: {user_id}")

if __name__ == "__main__":
    main()