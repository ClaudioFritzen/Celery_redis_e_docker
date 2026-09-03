from app.celery_app import app
import time

@app.task(name="app.tasks.add")
def add(x, y):
    time.sleep(3)
    return x + y


@app.task(queue='critical')
def process_payment(data):
    return f"Payment processed for {data['user']} with amount {data['amount']}"
