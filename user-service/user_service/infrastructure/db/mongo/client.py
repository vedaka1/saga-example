from functools import lru_cache

from pymongo.asynchronous.mongo_client import AsyncMongoClient

from user_service.main.config import MongoDBConfig


@lru_cache(1)
def init_mongo_db_client(config: MongoDBConfig = MongoDBConfig.load_from_env()) -> AsyncMongoClient:
    client: AsyncMongoClient = AsyncMongoClient(config.CONNECTION_URI, serverSelectionTimeoutMS=3000)
    return client
