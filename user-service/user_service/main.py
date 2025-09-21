from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from user_service.config import CONFIG
from user_service.infrastructure.db.mongo.client import init_mongo_db_client
from user_service.infrastructure.db.mongo.user.repository import MongoUserRepository
from user_service.presentation.http.error_handler import init_exc_handlers
from user_service.presentation.http.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    client = init_mongo_db_client()
    database = client[CONFIG.mongodb.USER_DB_NAME]
    await MongoUserRepository(database, CONFIG.mongodb)._create_indexes()
    yield
    await client.close()


def create_app() -> FastAPI:
    root_prefix = '/api'
    app = FastAPI(lifespan=lifespan)
    app.include_router(user_router, prefix=root_prefix)
    init_exc_handlers(app)
    return app
