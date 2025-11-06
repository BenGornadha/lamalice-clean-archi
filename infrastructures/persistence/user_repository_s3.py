from typing import Any

from domain.entities.user import UserRegistered
from domain.exceptions.user import UserNotFoundError
from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository
from infrastructures.serializers.user_serializer import UserSerializer
import json
class S3UserRepository(UserRepository):

    def __init__(self, s3_client: Any, bucket: str, user_serializer: UserSerializer) -> None:
        self._s3 = s3_client
        self._bucket = bucket
        self._user_serializer = user_serializer

    def _key_for(self, email: Email) -> str:
        return f"users/{str(email)}.json"

    def save(self, user: UserRegistered) -> None:
        serialized = self._user_serializer.serialize(user)
        key = self._key_for(user.email)
        self._s3.put_object(Bucket=self._bucket, Key=key, Body=json.dumps(serialized))

    def get(self, user: UserRegistered) -> UserRegistered:
        key = self._key_for(user.email)
        try:
            resp = self._s3.get_object(Bucket=self._bucket, Key=key)
            body = resp.get("Body")
            content = body.read().decode("utf-8")
            serialized = json.loads(content)
            return self._user_serializer.deserialize(serialized)
        except Exception:
            raise UserNotFoundError(user.uuid)

    def exists(self, email: Email) -> bool:
        key = self._key_for(email)
        try:
            self._s3.head_object(Bucket=self._bucket, Key=key)
            return True
        except Exception:
            return False

