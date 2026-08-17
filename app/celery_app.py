from celery import Celery
from kombu import Queue


app = Celery(
    'hello_celery',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='rpc://',
    #backend='redis://redis_queue:6379/1',
)

app.conf.task_queues = (
    Queue('critical', routing_key='critical', exchange='critical', durable=True),
    Queue('high', routing_key='high', exchange='high', durable=True),
    Queue('low', routing_key='low', exchange='low', durable=True),
)

app.conf.task_default_queue = 'low'
app.conf.task_default_exchange = 'low'
app.conf.task_default_routing_key = 'low'

app.conf.update(
    imports=["app.tasks"]
)