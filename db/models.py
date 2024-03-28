from sqlalchemy.orm import Mapped, mapped_column
from db.engine import Base
from uuid import UUID, uuid4

class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)
    password: Mapped[str] = mapped_column()
    username: Mapped[str | None] = mapped_column(unique=True)

