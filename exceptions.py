from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = 'user already exists!'


class UsernameOrPasswordIncorrect(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = 'username or password is incorrect'


class ArticleAlreadyExists(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = 'article already exists!'
