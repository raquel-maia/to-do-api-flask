def task_schema(task):

    due_date = task.get("due_date")
    created_at = task.get("created_at")

    return {
        "id": str(task["_id"]),
        "title": task.get("title"),
        "description": task.get("description"),
        "priority": task.get("priority"),
        "status": task.get("status"),
        "due_date": due_date.isoformat() if due_date else None,
        "created_at": created_at.isoformat() if created_at else None
    }


def tasks_schema(tasks):
    return [task_schema(task) for task in tasks]