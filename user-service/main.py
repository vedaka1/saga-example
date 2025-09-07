from fastapi import FastAPI

from user_service.presentation.api.handlers.error_handler import init_exc_handlers
from user_service.presentation.api.handlers.user.router import router as user_router


def create_app() -> FastAPI:
    root_prefix = '/api'
    app = FastAPI()
    app.include_router(user_router, prefix=root_prefix)
    init_exc_handlers(app)
    return app
