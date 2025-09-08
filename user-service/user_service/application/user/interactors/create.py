from dataclasses import dataclass

from user_service.application.user.dto import CreateUserInput
from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.common.error import ObjectAlreadyExistsError
from user_service.domain.user.entity import UserEntity


@dataclass
class CreateUserInteractor:
    user_repository: IUserRepository

    async def execute(self, create_data: CreateUserInput) -> UserEntity:
        user = await self.user_repository.get_by_username(create_data.username)
        if user:
            raise ObjectAlreadyExistsError(message=f'Пользователь с username: {create_data.username} уже существует')
        user = UserEntity(username=create_data.username, email=create_data.email)
        await self.user_repository.create(user)
        return user
