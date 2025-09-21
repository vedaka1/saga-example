from functools import lru_cache

from pymongo.asynchronous.mongo_client import AsyncMongoClient

from user_service.config import CONFIG, AppConfig


@lru_cache(1)
def init_mongo_db_client(config: AppConfig = CONFIG) -> AsyncMongoClient:
    client: AsyncMongoClient = AsyncMongoClient(config.mongodb.CONNECTION_URI, serverSelectionTimeoutMS=3000)
    return client
