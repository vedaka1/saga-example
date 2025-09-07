from pydantic import BaseModel


class UserFiltersSchema(BaseModel):
    username: str | None = None
