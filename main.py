from fastapi import FastAPI
from classmd.class_basemd import TaskAdd
from contextlib import asynccontextmanager
from repo import TaskRepo
from database.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.post('/tasks')
async def post_task(task: TaskAdd):
    task_id = await TaskRepo.add_one(task)
    return {'ok': True, 'task_id': task_id}

@app.get('/tasks')
async def get_tasks():
    tasks = await TaskRepo.find_all()
    return {'data': tasks}

@app.get('/task/{task_id}')
async def get_task(task_id: int):
    task = await TaskRepo.find_one(task_id)
    if not task:
        return {'error': 'Задача не найдена'}
    return {'data': task}

@app.delete('/task/{task_id}')
async def delete_task(task_id: int):
    is_deleted = await TaskRepo.delete_one(task_id)
    
    if not is_deleted:
        return {'error:' 'Нечего удалять, такой задачи нету'}
    return {'ok': True, 'message': 'Задача удалена'}

@app.put('/task/{task_id}')
async def update_task(task_id: int, task: TaskAdd):
    is_updated = await TaskRepo.update_one(task_id, task)
    if not is_updated:
        return {'error': 'Не найдена задача с таки ID'}
    return {'ok': True, 'message': 'Обновили'}