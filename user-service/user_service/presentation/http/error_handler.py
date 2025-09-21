from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from user_service.domain.common.error import ApplicationError


async def application_exception_handler(request: Request, exc: ApplicationError) -> JSONResponse:
    return JSONResponse(
        content={'status_code': exc.status_code, 'message': exc.message},
        status_code=exc.status_code,
    )


async def unknown_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(content='Unknown error occured', status_code=500)


def init_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApplicationError, cast(ExceptionHandler, application_exception_handler))
    app.add_exception_handler(Exception, cast(ExceptionHandler, unknown_exception_handler))
