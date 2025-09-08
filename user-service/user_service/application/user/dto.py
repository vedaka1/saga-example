from dataclasses import dataclass


@dataclass
class CreateUserInput:
    username: str
    email: str
