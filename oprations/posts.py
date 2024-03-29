from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Article
from schema.output import ArticleOutput



class ArticleOpration:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, title: str, content: str, status: bool):
        article = Article(
            title=title,
            content=content,
            status=status
        )
        async with self.db_session as session:
            # add exception !!
            session.add(article)
            await session.commit()

        return ArticleOutput(**article.__dict__)
     
            