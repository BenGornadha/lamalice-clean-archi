from uuid import UUID

from domain.entities.user import User
from domain.value_objects.email import Email
from infrastructures.serializers.user_serialized import UserSerialized
from interfaces.user_serializer import UserSerializer
from datetime import datetime


class UserJsonSerializer(UserSerializer):

    def serialize(self, user: User) -> dict:
        return {
            "uuid": str(user.uuid),
            "email": str(user.email),
            "registered_at": user.registered_at.isoformat(),
        }

    def deserialize(self, serialized_user : UserSerialized) -> User:
        return User(uuid=UUID(serialized_user.get("uuid")),
                    email=Email(serialized_user.get("email")),
                    registered_at=datetime.fromisoformat(serialized_user.get('registered_at')))

class NoSerializer(UserSerializer):

    def serialize(self, user: User):
        return user

    def deserialize(self, serialized_user : UserSerialized):
        return serialized_user