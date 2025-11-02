from pydantic import BaseModel

class UserSerialized(BaseModel):
    uuid: str
    email: str
    registered_at: str