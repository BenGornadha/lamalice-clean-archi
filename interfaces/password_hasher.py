from abc import ABC, abstractmethod


class PasswordHasherInterface(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        pass

