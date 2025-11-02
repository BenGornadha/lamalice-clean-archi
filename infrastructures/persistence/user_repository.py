from uuid import UUID

from domain.entities.user import User, NotFoundUser
from domain.exceptions.user import UserNotFoundError
from domain.value_objects.email import Email
from infrastructures.serializers.user_serialized import UserSerialized

from interfaces.user_repository import UserRepository
from infrastructures.serializers.user_serializer import UserSerializer


class InMemoryUserRepository(UserRepository):
    def __init__(self, user_serializer: UserSerializer) -> None:
        self._db: dict[Email, UserSerialized] = {}
        self._user_serializer = user_serializer

    def save(self, user: User) -> None:
        serialized_user = self._user_serializer.serialize(user)
        self._db[user.email] = serialized_user

    def get(self, user: User) -> User | NotFoundUser:
        result_user = self._db.get(user.email,NotFoundUser())
        if NotFoundUser() == result_user:
            raise UserNotFoundError(user_id=user.uuid)
        return self._user_serializer.deserialize(result_user)

    def exists(self, email: Email) -> bool:
        return email in self._db

