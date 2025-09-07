from motor.core import AgnosticClient
from sqlalchemy.ext.asyncio import AsyncSession

from user_service.application.common.interfaces.commiter import ICommiter


class Commiter(ICommiter):
    __slots__ = ('session',)

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def close(self) -> None:
        await self.session.close()


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
