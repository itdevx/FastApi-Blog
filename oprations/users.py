# Repository Pattern
# CRUD with Class

from sqlalchemy.ext.asyncio import AsyncSession # --> connection to database
from db.models import User
import sqlalchemy as sq
from fastapi.exceptions import ValidationException
from fastapi import HTTPException, status
from utils.secrets import password_manager
from schema.output import RegisterOutput
from sqlalchemy.exc import IntegrityError
from exceptions import UserAlreadyExists



class UsersOperation:
    def __init__(self, db_session:AsyncSession) -> None:
        self.db_session = db_session

    
    async def create(self, username:str, password:str) -> User:
        user_pwd = password_manager.hash(password)
        user = User(
            password=user_pwd,
            username=username,
        )
        async with self.db_session as session:
            # handled error for user exists
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                raise UserAlreadyExists

        # return RegisterOutput(username=user.username, id=user.id)
        return RegisterOutput(**user.__dict__)
    
    async def get_user_by_username(self, username: str) -> User:
        # SELECT * FROM User WHERE USER.username==string 
        query = sq.select(User).where(User.username == username)
        async with self.db_session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail='User not found')

            return user_data
        
        
    async def update_username(self, old_username:str, new_username:str) -> User:
        query = sq.select(User).where(User.username == old_username)
        update_query = sq.update(User).where(User.username == old_username).values(username=new_username)
        async with self.db_session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail='User not found')
                
            await session.execute(update_query)
            await session.commit()
            user_data.username = new_username
            return user_data
        
    
    async def delete(self, username:str, password: str) -> None:
        delete_query = sq.delete(User).where(username==username, password==password)
        async with self.db_session as session:
            await session.execute(delete_query)
            await session.commit()