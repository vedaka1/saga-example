from dataclasses import dataclass

from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.common.error import ObjectNotFoundError


@dataclass
class DeleteUserInteractor:
    user_repository: IUserRepository

    async def execute(self, user_id: str) -> None:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise ObjectNotFoundError(message='User not found')
        await self.user_repository.delete_by_id(user_id)
        return None
