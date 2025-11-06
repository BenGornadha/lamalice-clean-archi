import bcrypt
import hashlib
from interfaces.password_hasher import PasswordHasherInterface


class BcryptPasswordHasher(PasswordHasherInterface):
    def __init__(self, rounds: int = 12):
        self._rounds = rounds

    def hash(self, password: str) -> str:
        pw = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=self._rounds)
        return bcrypt.hashpw(pw, salt).decode('utf-8')


class SHA256PasswordHasher(PasswordHasherInterface):
    def __init__(self, salt: str = "default_salt"):
        self._salt = salt

    def hash(self, password: str) -> str:
        salted_password = password + self._salt
        return hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
