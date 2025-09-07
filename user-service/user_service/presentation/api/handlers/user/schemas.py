from dataclasses import dataclass

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    email: str


@dataclass
class UserResponse:
    id: str
    username: str
    email: str
