from typing import Any
import logging

from domain.entities.user import UserRegistered, NotFoundUser
from domain.exceptions.user import UserNotFoundError
from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository
from infrastructures.serializers.user_serializer import UserSerializer
from infrastructures.serializers.user_serialized import UserSerialized

logger = logging.getLogger(__name__)


class BigQueryUserRepository(UserRepository):

    def __init__(self, client: Any, dataset: str, table: str, user_serializer: UserSerializer) -> None:
        self._client = client
        self._dataset = dataset
        self._table = table
        self._user_serializer = user_serializer

    def save(self, user: UserRegistered) -> None:
        serialized = self._user_serializer.serialize(user)
        table_ref = f"{self._dataset}.{self._table}"
        self._client.insert_rows_json(table_ref, [serialized])

    def get(self, user: UserRegistered) -> UserRegistered:
        rows = self._query(user)
        if not rows:
            raise UserNotFoundError(user_id=user.uuid)
        row = rows[0]
        serialized = UserSerialized(**{
            "uuid": row.get("uuid"),
            "email": row.get("email"),
            "registered_at": row.get("registered_at"),
        })
        return self._user_serializer.deserialize(serialized)

    def exists(self, email: Email) -> bool:
        sql = f"SELECT 1 FROM `{self._dataset}.{self._table}` WHERE email = @email LIMIT 1"
        result = self._client.query(sql, params={"email": str(email)})
        return len(list(result)) > 0

    def _query(self, user: UserRegistered) -> list[dict]:
        sql = f"SELECT uuid, email, registered_at FROM `{self._dataset}.{self._table}` WHERE email = @email LIMIT 1"
        params = {"email": str(user.email)}
        result = self._client.query(sql, params=params)
        return list(result)

