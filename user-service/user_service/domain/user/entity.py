from uuid import uuid4


class UserEntity:
    def __init__(self, username: str, email: str, id: str | None = None) -> None:
        self._id = id or str(uuid4())
        self.username = username
        self.email = email

    @property
    def id(self) -> str:
        if not self._id:
            raise Exception('No identity')
        return self._id
