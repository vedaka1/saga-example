from dataclasses import dataclass


@dataclass
class UserFilters:
    username: str | None = None
    username_ilike: str | None = None
