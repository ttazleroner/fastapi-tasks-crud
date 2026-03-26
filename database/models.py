from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class TaskORM(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    is_completed: Mapped[bool] = mapped_column(default=False)