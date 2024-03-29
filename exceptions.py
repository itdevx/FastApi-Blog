from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = 'user already exists!'


class UsernameOrPasswordIncorrect(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = 'username or password is incorrect'
