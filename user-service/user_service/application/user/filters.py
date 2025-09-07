from dataclasses import dataclass


@dataclass
class UserFiltersDTO:
    username: str | None = None
