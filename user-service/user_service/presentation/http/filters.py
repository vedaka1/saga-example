from pydantic import BaseModel

from user_service.application.user.filters import UserFilters


class UserFiltersRequest(BaseModel):
    username: str | None = None

    def to_dto(self) -> UserFilters:
        return UserFilters(
            username=self.username,
        )
