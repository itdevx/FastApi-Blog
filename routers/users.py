from fastapi  import APIRouter, Body, Depends
from schema._input import UserInput, UpdateUserProfileInput, DeleteUserAccountInput
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from oprations.users import UsersOperation


router = APIRouter()


@router.post('/register')
async def register(db_session: Annotated[AsyncSession, Depends(get_db)], data: UserInput = Body()):
    user = await UsersOperation(db_session).create(
        username=data.username,
        password=data.password
    )
    return user


@router.post('/login')
async def login(db_session: Annotated[AsyncSession, Depends(get_db)], data: UserInput = Body()):
    token = await UsersOperation(db_session).login(data.username, data.password)
    return token


@router.get('/{username}/')
async def get_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)], username: str):
    user_profile = await UsersOperation(db_session=db_session).get_user_by_username(username=username)
    return user_profile


@router.put('/update-profile/')
async def user_update_profile(db_session: Annotated[AsyncSession, Depends(get_db)], data: UpdateUserProfileInput = Body()):
    user = await UsersOperation(db_session).update_username(old_username=data.old_username, new_username=data.new_username)
    return user


@router.delete('/delete/')
async def delete_user_account(db_session: Annotated[AsyncSession, Depends(get_db)], data: DeleteUserAccountInput = Body()):
    await UsersOperation(db_session).delete(username=data.username, password=data.password)
