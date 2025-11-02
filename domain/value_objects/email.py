import dataclasses


@dataclasses.dataclass(frozen=True)
class Email:
    address: str
