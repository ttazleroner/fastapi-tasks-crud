from database.database import new_session, TaskORM
from classmd.class_basemd import TaskAdd
from sqlalchemy import select, delete, update

class TaskRepo:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
            
    
    @classmethod
    async def find_all(cls, limit: int =  100, offset: int = 0):
        async with new_session() as session:
            
            query = select(TaskORM).limit(limit).offset(offset)
            
            
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
    
    @classmethod
    async def find_one(cls, task_id: int):
        async with new_session() as session:
            query = select(TaskORM).where(TaskORM.id == task_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def delete_one(cls, task_id: int) -> bool:
        async with new_session() as session:
            query = delete(TaskORM).where(TaskORM.id == task_id)
            
            result = await session.execute(query)
            
            await session.commit()
            
            return result.rowcount > 0
    
    @classmethod
    async def update_one(cls, task_id: int, data: TaskAdd):
        async with new_session() as session:
            query = update(TaskORM).where(TaskORM.id == task_id).values(**data.model_dump()).returning(TaskORM)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()
    
    @classmethod
    async def find_active(cls, is_completed: bool):
        async with new_session() as session:
            query = select(TaskORM).where(TaskORM.is_completed == is_completed)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models