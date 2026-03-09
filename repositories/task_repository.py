
from config.database import tasks_collection
from bson import ObjectId


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

def update_task(task_id, data):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": data}
    )
    return tasks_collection.find_one({"_id": ObjectId(task_id)})
    
def delete_task (task_id):
    result = tasks_collection.delete_one({"_id":ObjectId(task_id)})
    return result.deleted_count > 0

def get_task_by_id(task_id):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})