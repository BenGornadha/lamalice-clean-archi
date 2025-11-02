import dataclasses
import datetime
from typing import Any
from uuid import UUID
from domain.value_objects.email import Email

@dataclasses.dataclass
class User:
    uuid: UUID
    email: Email
    registered_at : datetime.datetime


@dataclasses.dataclass
class NotFoundUser:
    ...

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__)