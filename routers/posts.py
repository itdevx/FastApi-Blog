from fastapi import APIRouter, Body, Depends
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from schema._input import Article
from oprations.posts import ArticleOpration


router = APIRouter()


@router.post('/create-article')
async def create_article(db_session: Annotated[AsyncSession, Depends(get_db)], data: Article = Body()):
    article = await ArticleOpration(db_session).create(title=data.title, content=data.content, status=data.status)
    return article

