from dataclasses import dataclass

from user_service.application.common.interfaces.commiter import ICommiter
from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.common.error import ObjectAlreadyExistsError
from user_service.domain.user.entity import UserEntity
from user_service.presentation.api.handlers.user.schemas import UserCreateSchema


@dataclass
class CreateUserInteractor:
    user_repository: IUserRepository
    commiter: ICommiter

    async def execute(self, create_data: UserCreateSchema) -> UserEntity:
        user = await self.user_repository.get_by_username(create_data.username)
        if user:
            raise ObjectAlreadyExistsError(message=f'Пользователь с username: {create_data.username} уже существует')
        user = UserEntity(username=create_data.username, email=create_data.email)
        await self.user_repository.create(user)
        await self.commiter.commit()
        return user
