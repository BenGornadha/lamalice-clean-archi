from abc import ABC, abstractmethod

from domain.entities.user import UserRegistered
from domain.value_objects.email import Email


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: UserRegistered) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get(self, user: UserRegistered) -> UserRegistered:
        raise NotImplementedError()

    @abstractmethod
    def exists(self, email: Email) -> bool:
        raise NotImplementedError()

