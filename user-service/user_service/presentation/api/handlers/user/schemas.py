from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    username: str
    email: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
