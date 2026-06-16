from celery import Celery


app = Celery(
    'hello_celery',
    broker='redis://redis_queue:6379/0',
    backend='redis://redis_queue:6379/1',
)

app.conf.update(
    imports=["app.tasks"]
)