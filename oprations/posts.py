from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Article
from schema.output import ArticleOutput
from sqlalchemy.exc import IntegrityError
from exceptions import ArticleAlreadyExists



class ArticleOpration:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, title: str, content: str, status: bool) -> Article:
        article = Article(
            title=title,
            content=content,
            status=status
        )
        async with self.db_session as session:
            try:
                session.add(article)
                await session.commit()
            except IntegrityError:
                raise ArticleAlreadyExists

        return ArticleOutput(**article.__dict__)
     
            