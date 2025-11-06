import bcrypt
from interfaces.password_hasher import PasswordHasherInterface


class BcryptPasswordHasher(PasswordHasherInterface):
    def __init__(self, rounds: int = 12):
        self._rounds = rounds

    def hash(self, password: str) -> str:
        pw = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=self._rounds)
        return bcrypt.hashpw(pw, salt).decode('utf-8')
