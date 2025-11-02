from dataclasses import dataclass

@dataclass
class UserSerialized:
    uuid: str
    email: str
    registered_at: str