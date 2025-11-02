from abc import ABC, abstractmethod

from domain.entities.user import User
from infrastructures.serializers.user_serialized import UserSerialized


class UserSerializer(ABC):

    @abstractmethod
    def serialize(self, user: User) :
        raise NotImplementedError

    def deserialize(self, serialized_user : UserSerialized) -> User:
        raise  NotImplementedError