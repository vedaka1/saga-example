from pydantic import BaseModel

from user_service.application.user.dto import CreateUserInput


class UserCreateRequest(BaseModel):
    username: str
    email: str

    def to_dto(self) -> CreateUserInput:
        return CreateUserInput(
            username=self.username,
            email=self.email,
        )
