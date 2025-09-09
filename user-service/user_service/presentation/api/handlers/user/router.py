from fastapi import APIRouter, Depends

from user_service.application.user.interactors.create import CreateUserInteractor
from user_service.application.user.interactors.delete_one import DeleteUserInteractor
from user_service.application.user.interactors.get_many import GetUsersInteractor, UserFilters
from user_service.application.user.interactors.get_one import GetUserInteractor
from user_service.domain.common.error import ApplicationError, ObjectAlreadyExistsError, ObjectNotFoundError
from user_service.infrastructure.db.commiter import MongoCommiter
from user_service.infrastructure.db.mongo.client import init_mongo_db_client
from user_service.infrastructure.db.mongo.user.__ini__ import init_user_repository
from user_service.presentation.api.handlers.user.filters import UserFiltersSchema
from user_service.presentation.api.handlers.user.schemas import UserCreateRequest, UserResponse

router = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    '',
    summary='Создание пользователя',
    responses={
        200: {'model': str},
        400: {'model': ApplicationError, 'description': ObjectAlreadyExistsError.message},
    },
)
async def create_user(create_data: UserCreateRequest) -> str:
    client = init_mongo_db_client()
    user_repository = init_user_repository()
    interactor = CreateUserInteractor(user_repository, MongoCommiter(client))
    user = await interactor.execute(create_data)
    return user.id


@router.get(
    '/{user_id}',
    summary='Получение пользователя по ID',
    responses={
        200: {'model': UserResponse},
        404: {'model': ApplicationError, 'description': ObjectNotFoundError.message},
    },
)
async def get_user(user_id: str) -> UserResponse:
    user_repository = init_user_repository()
    interactor = GetUserInteractor(user_repository)
    user = await interactor.execute(user_id)
    return UserResponse(id=user.id, username=user.username, email=user.email)


@router.get(
    '',
    summary='Получение списка пользователей',
    responses={
        200: {'model': UserResponse},
    },
)
async def get_users(
    filters: UserFiltersSchema = Depends(),
    offset: int = 0,
    limit: int | None = 100,
) -> list[UserResponse]:
    user_repository = init_user_repository()
    interactor = GetUsersInteractor(user_repository)
    users = await interactor.execute(filters=UserFilters(filters.username), offset=offset, limit=limit)
    return [UserResponse(id=user.id, username=user.username, email=user.email) for user in users]


@router.delete(
    '/{user_id}',
    summary='Удаление пользователя по ID',
    responses={
        200: {'model': UserResponse},
        404: {'model': ApplicationError, 'description': ObjectNotFoundError.message},
    },
)
async def delete_user(user_id: str) -> None:
    user_repository = init_user_repository()
    interactor = DeleteUserInteractor(user_repository)
    await interactor.execute(user_id)
    return None
