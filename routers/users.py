from fastapi  import APIRouter, Body, Depends
from schema._input import RegisterInput
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from oprations.users import UsersOperation


router = APIRouter()


@router.post('/register')
async def register(db_session: Annotated[AsyncSession, Depends(get_db)], data: RegisterInput = Body()):
    user = await UsersOperation(db_session).create(
        username=data.username,
        password=data.password
    )
    return user


@router.post('/login')
async def login():
    ...


@router.get('/{username}')
async def get_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)], username: str):
    user_profile = await UsersOperation(db_session=db_session).get_user_by_username(username=username)
    return user_profile


@router.put('/update-profile')
async def user_update_profile():
    ...