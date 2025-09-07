from pydantic import BaseModel


class UserFilters(BaseModel):
    username: str | None = None
