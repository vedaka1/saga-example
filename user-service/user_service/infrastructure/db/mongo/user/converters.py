from user_service.domain.user.entity import UserEntity


def user_entity_to_dict(entity: UserEntity) -> dict:
    return {
        '_id': entity.id,
        'username': entity.username,
        'email': entity.email,
    }


def dict_to_user_entity(data: dict) -> UserEntity:
    return UserEntity(
        id=data['_id'],
        username=data['username'],
        email=data['email'],
    )
