from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


engine = create_async_engine(
    'sqlite+aiosqlite:///tasks.db'
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class TaskORM(Model):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    desc: Mapped[Optional[str]]
    is_completed: Mapped[bool] = mapped_column(default=False)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)