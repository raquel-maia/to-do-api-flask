
from config.database import tasks_collection


def list_tasks(status=None):
    if status:
        query = {"status": status}
    else:
        query = {}
    
    return list(tasks_collection.find(query))

def create_task(task_data):
    result = tasks_collection.insert_one(task_data)
    return result.inserted_id

def find_task_by_title(title):
    return tasks_collection.find_one({"title": title})