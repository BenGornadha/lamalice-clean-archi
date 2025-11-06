from abc import ABC, abstractmethod

from domain.entities.user import UserRegistered
from infrastructures.serializers.user_serialized import UserSerialized


class UserSerializer(ABC):

    @abstractmethod
    def serialize(self, user: UserRegistered) :
        raise NotImplementedError

    @abstractmethod
    def deserialize(self, serialized_user : UserSerialized) -> UserRegistered:
        raise  NotImplementedError