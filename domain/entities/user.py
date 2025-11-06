import dataclasses
import datetime
from typing import Any
from uuid import UUID
from domain.value_objects.email import Email

@dataclasses.dataclass(frozen=True)
class UserInput:
    email: str
    password: str

@dataclasses.dataclass(frozen=True)
class UserRegistered:
    uuid: UUID
    email: Email
    registered_at : datetime.datetime
    password_hash: str


@dataclasses.dataclass
class NotFoundUser:
    ...

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__)