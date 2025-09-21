from dataclasses import dataclass, field

from user_service.environment import get_env_var

# class PostgresqlConfig:
#     POSTGRES_HOST: str = get_env_var('POSTGRES_HOST', str, default='postgres')
#     POSTGRES_PORT: int = get_env_var('POSTGRES_PORT', int, default=5432)
#     POSTGRES_USER: str = get_env_var('POSTGRES_USER', str)
#     POSTGRES_PASSWORD: str = get_env_var('POSTGRES_PASSWORD', str)
#     POSTGRES_DB: str = get_env_var('POSTGRES_DB', str)

#     @property
#     def DB_URL(self) -> str:
#         return 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}'.format(
#             user=self.POSTGRES_USER,
#             password=self.POSTGRES_PASSWORD,
#             host=self.POSTGRES_HOST,
#             port=self.POSTGRES_PORT,
#             db=self.POSTGRES_DB,
#         )


@dataclass
class MongoDBConfig:
    CONNECTION_URI: str = field(
        default=get_env_var('MONGO_DB_CONNECTION_URI', str, default='mongodb://localhost:27017')
    )
    ADMIN_USERNAME: str = field(default=get_env_var('MONGO_DB_ADMIN_USERNAME', str, default='admin'))
    ADMIN_PASSWORD: str = field(default=get_env_var('MONGO_DB_ADMIN_PASSWORD', str, default='admin'))
    USER_DB_NAME: str = field(default=get_env_var('USER_DB_NAME', str, default='user_service'))
    USER_COLLECTION_NAME: str = field(default=get_env_var('USER_COLLECTION_NAME', str, default='user'))


@dataclass
class AppConfig:
    mongodb: MongoDBConfig = field(default_factory=MongoDBConfig)


CONFIG = AppConfig()
