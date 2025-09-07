from abc import abstractmethod
from typing import Protocol

from user_service.application.user.filters import UserFiltersDTO
from user_service.domain.user.entity import UserEntity


class IUserRepository(Protocol):
    @abstractmethod
    async def create(self, user: UserEntity) -> None: ...

    @abstractmethod
    async def get_by_id(self, entity_id: str) -> UserEntity | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> UserEntity | None: ...

    @abstractmethod
    async def get_many(self, filters: UserFiltersDTO, offset: int, limit: int | None = None) -> list[UserEntity]: ...
