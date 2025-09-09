from pymongo import ASCENDING
from pymongo.asynchronous.client_session import AsyncClientSession
from pymongo.asynchronous.database import AsyncDatabase

from user_service.application.user.filters import UserFilters
from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.user.entity import UserEntity
from user_service.infrastructure.db.mongo.filters.build import build_mongo_filters
from user_service.infrastructure.db.mongo.user.converters import dict_to_user_entity, user_entity_to_dict
from user_service.infrastructure.db.mongo.user.filters import UserFiltersMongo
from user_service.main.config import init_config


class MongoUserRepository(IUserRepository):
    __slots__ = ('database', '_collection', '_session')

    def __init__(
        self,
        database: AsyncDatabase,
        *,
        collection_name: str = init_config().mongodb.USER_COLLECTION_NAME,
        session: AsyncClientSession | None = None,
    ) -> None:
        self._collection = database[collection_name]
        self._session = session

    async def _create_indexes(self) -> None:
        await self._collection.create_index([('username', ASCENDING)], unique=True, session=self._session)
        await self._collection.create_index([('email', ASCENDING)], unique=True, session=self._session)

    async def create(self, user: UserEntity) -> None:
        data = user_entity_to_dict(user)
        await self._collection.insert_one(data, session=self._session)

    async def _get_by(self, key: str, value: str) -> UserEntity | None:
        if user := await self._collection.find_one({key: value}, session=self._session):
            return dict_to_user_entity(user)
        else:
            return None

    async def _delete_by(self, key: str, value: str) -> UserEntity | None:
        await self._collection.delete_one({key: value}, session=self._session)
        return None

    async def delete_by_id(self, entity_id: str) -> UserEntity | None:
        return await self._delete_by('_id', entity_id)

    async def get_by_id(self, entity_id: str) -> UserEntity | None:
        return await self._get_by('_id', entity_id)

    async def get_by_username(self, username: str) -> UserEntity | None:
        return await self._get_by('username', username)

    async def get_many(self, filters: UserFilters, offset: int = 0, limit: int | None = None) -> list[UserEntity]:
        users: list[UserEntity] = []
        _filters = build_mongo_filters(filters, UserFiltersMongo)
        cursor = self._collection.find(_filters, session=self._session).skip(offset)
        if limit:
            cursor.limit(limit)

        async for user in cursor:
            users.append(dict_to_user_entity(user))
        return users
