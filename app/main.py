# main.py

from fastapi import FastAPI

from app.tasks.tasks import add
from app.tasks.tasks import process_payment
from app.celery_app import app as celery_app
from app.routers import (
    user,
)

api = FastAPI()
api.include_router(user.router)

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

    process_payment.apply_async(args=[{'user': 'John Doe', 'amount': 100}], queue='critical') #agora a task será enviada para a fila 'critical'
    
    return {f'Task sent to critical queue': 'Check your RabbitMQ dashboard for the task status.'} 



@api.get('/ola_mundo')
async def ola_mundo():
    return {'message': 'Olá, Mundo!'}   