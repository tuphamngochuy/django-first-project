from dataclasses import dataclass
from typing import TypedDict

@dataclass
class RegisterUserInput(TypedDict): 
    username: str
    password: str
    display_name: str


@dataclass
class CreateUserInput(TypedDict):
    username: str
    display_name: str
    password: str
    salt: str