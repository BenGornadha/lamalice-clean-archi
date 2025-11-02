from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterUserInput:
    email: str
    password: str