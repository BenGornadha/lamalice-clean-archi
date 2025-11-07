import dataclasses


@dataclasses.dataclass(frozen=True)
class UserInput:
    email: str
    password: str
