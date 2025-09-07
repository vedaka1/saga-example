from dataclasses import dataclass

from user_service.application.user.filters import UserFilters
from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.user.entity import UserEntity


@dataclass
class GetUsersInteractor:
    user_repository: IUserRepository

    async def execute(self, filters: UserFilters, offset: int, limit: int | None) -> list[UserEntity]:
        users = await self.user_repository.get_many(filters=filters, offset=offset, limit=limit)
        return users
