# main.py

from fastapi import FastAPI
from app.models import UserCreate
from app.rabbitmq import publish_user_created
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


@api.get('/rabbitmq/critical')
async def run_critical_task():
    task = celery_app.send_task('app.tasks.process_payment', args=[{'user': 'John Doe', 'amount': 100}], queue='critical')
    return {'task_id': task.id} 



@api.post('/users')
async def create_user(data: UserCreate):

    user_id = 123 

    publish_user_created(user_id, data.email)
    pass

@api.get('/ola_mundo')
async def ola_mundo():
    return {'message': 'Olá, Mundo!'}   