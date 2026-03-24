from fastapi import FastAPI, Depends
from typing import Annotated
from classmd.class_basemd import Task, TaskAdd
from contextlib import asynccontextmanager
from database.database import create_table
from repo import TaskRepo
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    print('База готова к работе')
    yield
    print('Выключение')

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