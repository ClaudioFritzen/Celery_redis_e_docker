from celery import Celery


app = Celery(
    'hello_celery',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='rpc://',
    #backend='redis://redis_queue:6379/1',
)

app.conf.update(
    imports=["app.tasks"]
)