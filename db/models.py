from sqlalchemy.orm import Mapped, mapped_column
from db.engine import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    password: Mapped[str] = mapped_column()
    username: Mapped[str | None] = mapped_column(unique=True, default=None, nullable=True)

