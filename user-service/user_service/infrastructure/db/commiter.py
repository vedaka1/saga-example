from motor.core import AgnosticClient

from user_service.application.common.interfaces.commiter import ICommiter


class MongoCommiter(ICommiter):
    __slots__ = ('client',)

    def __init__(self, client: AgnosticClient) -> None:
        self.client = client

    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass

    async def close(self) -> None:
        self.client.close()
