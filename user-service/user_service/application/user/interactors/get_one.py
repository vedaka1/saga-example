from dataclasses import dataclass

from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.common.error import ObjectNotFoundError
from user_service.domain.user.entity import UserEntity


@dataclass
class GetUserInteractor:
    user_repository: IUserRepository

    async def execute(self, user_id: str) -> UserEntity:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise ObjectNotFoundError(message='User not found')
        return user
