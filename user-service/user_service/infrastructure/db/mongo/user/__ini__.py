from functools import lru_cache

from motor.core import AgnosticClient

from user_service.infrastructure.db.mongo.client import init_mongo_db_client
from user_service.infrastructure.db.mongo.user.repository import MongoUserRepository
from user_service.main.config import MongoDBConfig


@lru_cache(1)
def init_user_repository(
    config: MongoDBConfig = MongoDBConfig.load_from_env(),
    client: AgnosticClient = init_mongo_db_client(),
) -> MongoUserRepository:
    return MongoUserRepository(client, config.USER_DB_NAME, config.USER_COLLECTION_NAME)
