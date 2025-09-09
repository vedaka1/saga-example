from pymongo.asynchronous.client_session import AsyncClientSession

from user_service.application.common.interfaces.commiter import ICommiter


class MongoCommiter(ICommiter):
    __slots__ = ('_session',)

    def __init__(self, session: AsyncClientSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit_transaction()

    async def rollback(self) -> None:
        await self._session.abort_transaction()

    async def close(self) -> None:
        await self._session.end_session()
