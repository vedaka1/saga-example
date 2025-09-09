from pydantic import BaseModel

from user_service.domain.user.entity import UserEntity


class UserResponse(BaseModel):
    id: str
    username: str
    email: str

    @classmethod
    def from_entity(cls, user: UserEntity) -> 'UserResponse':
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
        )


class UsersResponse(BaseModel):
    items: list[UserResponse]
