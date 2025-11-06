from uuid import UUID

from domain.entities.user import UserRegistered
from domain.value_objects.email import Email
from infrastructures.serializers.user_serialized import UserSerialized
from interfaces.user_serializer import UserSerializer
from datetime import datetime


class UserJsonSerializer(UserSerializer):

    def serialize(self, user: UserRegistered) -> dict:
        return {
            "uuid": str(user.uuid),
            "email": str(user.email),
            "registered_at": user.registered_at.isoformat(),
            "password_hash": str(user.password_hash)
        }

    def deserialize(self, serialized_user : UserSerialized) -> UserRegistered:
        return UserRegistered(uuid=UUID(serialized_user.get("uuid")),
                              email=Email(serialized_user.get("email")),
                              registered_at=datetime.fromisoformat(serialized_user.get('registered_at')),
                              password_hash=serialized_user.get("password_hash"))

class NoSerializer(UserSerializer):

    def serialize(self, user: UserRegistered):
        return user

    def deserialize(self, serialized_user : UserSerialized):
        return serialized_user