from dataclasses import dataclass

from user_service.domain.common.error import ApplicationError


@dataclass
class UserError(ApplicationError):
    message: str = 'User error occured'
