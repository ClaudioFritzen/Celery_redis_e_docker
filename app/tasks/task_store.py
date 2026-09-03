# task_store.py

tasks_memory = []

def save_task(task_id, description):
    tasks_memory.append({
        "task_id": task_id,
        "description": description,
        "status": "PENDING"
    })

def update_task(task_id, status):
    for t in tasks_memory:
        if t["task_id"] == task_id:
            t["status"] = status
            break

def list_tasks():
    return tasks_memory
