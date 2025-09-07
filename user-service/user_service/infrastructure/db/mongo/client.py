from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient

from user_service.main.config import MongoDBConfig


@lru_cache(1)
def init_mongo_db_client(config: MongoDBConfig = MongoDBConfig.load_from_env()) -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient(config.CONNECTION_URI, serverSelectionTimeoutMS=3000)
    return client
