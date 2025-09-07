from motor.core import AgnosticClient, AgnosticCollection

from user_service.application.user.filters import UserFilters
from user_service.application.user.interfaces.repository import IUserRepository
from user_service.domain.user.entity import UserEntity
from user_service.infrastructure.db.mongo.filters.build import build_mongo_filters
from user_service.infrastructure.db.mongo.user.converters import dict_to_user_entity, user_entity_to_dict
from user_service.infrastructure.db.mongo.user.filters import UserFiltersMongo


class MongoUserRepository(IUserRepository):
    __slots__ = ('_client', '_db_name', '_collection_name')

    def __init__(self, client: AgnosticClient, db_name: str, collection_name: str) -> None:
        self._client = client
        self._db_name = db_name
        self._collection_name = collection_name

    @property
    def _collection(self) -> AgnosticCollection:
        return self._client[self._db_name][self._collection_name]

    async def create(self, user: UserEntity) -> None:
        data = user_entity_to_dict(user)
        await self._collection.insert_one(data)

    async def _get_by(self, key: str, value: str) -> UserEntity | None:
        if user := await self._collection.find_one({key: value}):
            return dict_to_user_entity(user)
        else:
            return None

    async def _delete_by(self, key: str, value: str) -> UserEntity | None:
        await self._collection.delete_one({key: value})
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
        cursor = self._collection.find(_filters).skip(offset)
        if limit:
            cursor.limit(limit)

        async for user in cursor:
            users.append(dict_to_user_entity(user))
        return users
