from dataclasses import dataclass


@dataclass
class ApplicationError(Exception):
    status_code: int = 500
    message: str = 'Internal Server Error'


@dataclass
class ObjectNotFoundError(ApplicationError):
    status_code: int = 404
    message: str = 'Object not found'


@dataclass
class ObjectAlreadyExistsError(ApplicationError):
    status_code: int = 400
    message: str = 'Object already exists'
