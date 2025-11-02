from abc import ABC, abstractmethod

from domain.entities.user import User
from domain.value_objects.email import Email


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def exists(self, email: Email) -> bool:
        raise NotImplementedError()

