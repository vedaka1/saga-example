from fastapi import APIRouter, Depends
from user_service.application.user.interactors.create import CreateUserInteractor
from user_service.application.user.interactors.delete_one import DeleteUserInteractor
from user_service.application.user.interactors.get_many import GetUsersInteractor
from user_service.application.user.interactors.get_one import GetUserInteractor
from user_service.domain.common.error import ApplicationError, ObjectAlreadyExistsError, ObjectNotFoundError
from user_service.infrastructure.db.mongo.client import init_mongo_db_client
from user_service.infrastructure.db.mongo.user.repository import MongoUserRepository
from user_service.main.config import init_config
from user_service.presentation.api.handlers.user.filters import UserFiltersRequest
from user_service.presentation.api.handlers.user.requests import UserCreateRequest
from user_service.presentation.api.handlers.user.responses import UserResponse, UsersResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    summary="Создание пользователя",
    responses={
        200: {"model": UserResponse},
        400: {"model": ApplicationError, "description": ObjectAlreadyExistsError.message},
    },
)
async def create_user(create_data: UserCreateRequest) -> UserResponse:
    client = init_mongo_db_client()
    database = client[init_config().mongodb.USER_DB_NAME]
    async with client.start_session() as session:
        interactor = CreateUserInteractor(MongoUserRepository(database, session=session))
        user = await interactor.execute(create_data.to_dto())
    return UserResponse.from_entity(user)


@router.get(
    "/{user_id}",
    summary="Получение пользователя по ID",
    responses={
        200: {"model": UserResponse},
        404: {"model": ApplicationError, "description": ObjectNotFoundError.message},
    },
)
async def get_user(user_id: str) -> UserResponse:
    client = init_mongo_db_client()
    database = client[init_config().mongodb.USER_DB_NAME]
    interactor = GetUserInteractor(MongoUserRepository(database))
    user = await interactor.execute(user_id)
    return UserResponse.from_entity(user)


@router.get(
    "",
    summary="Получение списка пользователей",
    responses={
        200: {"model": UsersResponse},
    },
)
async def get_users(
    filters: UserFiltersRequest = Depends(),
    offset: int = 0,
    limit: int | None = 100,
) -> UsersResponse:
    client = init_mongo_db_client()
    database = client[init_config().mongodb.USER_DB_NAME]
    interactor = GetUsersInteractor(MongoUserRepository(database))
    users = await interactor.execute(filters=filters.to_dto(), offset=offset, limit=limit)
    return UsersResponse(items=[UserResponse.from_entity(user) for user in users])


@router.delete(
    "/{user_id}",
    summary="Удаление пользователя по ID",
    responses={
        200: {"model": UserResponse},
        404: {"model": ApplicationError, "description": ObjectNotFoundError.message},
    },
)
async def delete_user(user_id: str) -> None:
    client = init_mongo_db_client()
    database = client[init_config().mongodb.USER_DB_NAME]
    interactor = DeleteUserInteractor(MongoUserRepository(database))
    await interactor.execute(user_id)
    return None
