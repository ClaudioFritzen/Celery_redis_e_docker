# app.py

from fastapi import FastAPI
from app.tasks import add
from app.celery_app import app as celery_app

api = FastAPI()

@api.post('/add')
async def run_add(x:int, y:int):
    task = add.delay(x, y)
    return {'task_id': task.id}


@api.get('/result/{task_id}')
async def get_result(task_id: str):
    result = add.AsyncResult(task_id, app=celery_app)

    return {
        'task_id': task_id,
        'status': result.status,
        'result': result.result
    }

@api.post("/add/batch")
async def run_batch():
    task_ids = []

    for i in range(10):
        task = add.delay(i, i * 2)
        task_ids.append(task.id)

    return {"tasks": task_ids}
