from abc import ABC, abstractmethod


class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, *args, **kwargs) -> None:
        raise NotImplementedError


class UserValidatorInterface(ValidatorInterface):

    ...

class PasswordValidatorInterface(ValidatorInterface):

    ...