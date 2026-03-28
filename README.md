# fastapi-tasks-crud
Learning project: FastAPI CRUD for tasks (async SQLAlchemy + SQLite)

FastAPI Tasks CRUD (learning project)

stack
- Python 3.11
- FastAPI
- Uvicorn
- SQLAlchemy 2.x (async)
- PostgreSQL

Features
- создание задачи
- получение списка задач (пагинация: limit/offset)
- получение задачи по id
- обновление задачи
- удаление задачи

API
после запуска открой:
- Swagger: http://127.0.0.1:8000/docs
- UPD - будет по дефолту в консоли

эндпоинты:
- `POST /tasks` — создать задачу
- `GET /tasks` — список задач
- `GET /task/{task_id}` — получить задачу
- `PUT /task/{task_id}` — обновить задачу
- `DELETE /task/{task_id}` — удалить задачу

Run locally

1) create venv & install deps
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
2)start server
bash

uvicorn main:app --reload
notes
база PostgreSQL создаётся автоматически при стартею
