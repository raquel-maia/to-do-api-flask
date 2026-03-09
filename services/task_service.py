from datetime import datetime, timezone
from repositories import task_repository
from schemas.task_schema import task_schema, tasks_schema

class TaskService:
    ALLOWED_STATUS = ["pending", "in_progress", "completed", "cancelled"]
    ALLOWED_PRIORITY = ["low", "medium", "high"]

    def list_all_tasks(self, status=None):
        if status and status not in self.ALLOWED_STATUS:
            raise ValueError(f"Status '{status}' inválido.")
        tasks = task_repository.list_tasks(status=status)
        return tasks_schema(tasks)

    def create_task(self, data):
        title = data.get("title", "").strip()
        status = data.get("status", "pending")
        priority = data.get("priority", "medium")
        
        if not title:
            raise ValueError("O título é obrigatório.")
        
        if task_repository.find_task_by_title(title):
            raise ValueError("Esse título já existe.")

        if status not in self.ALLOWED_STATUS:
            raise ValueError(f"Status inválido. Permitidos: {self.ALLOWED_STATUS}")

        # Conversão de data para o banco
        due_date_str = data.get("due_date")
        due_date = datetime.fromisoformat(due_date_str.replace('Z', '+00:00')) if due_date_str else None

        new_task = {
            "title": title,
            "description": data.get("description"),
            "priority": priority,
            "status": status,
            "due_date": due_date,
            "created_at": datetime.now(timezone.utc)
        }

        task_id = task_repository.create_task(new_task)
        new_task["_id"] = task_id
        return task_schema(new_task)

    def update_task_service(self, task_id, data):
        existing_task = task_repository.get_task_by_id(task_id)
        if not existing_task:
            raise ValueError("Tarefa não encontrada.")
        
        if existing_task["status"] == "completed":
            raise ValueError("Tarefas concluídas não podem ser editadas.")

    
        if "status" in data and data["status"] not in self.ALLOWED_STATUS:
            raise ValueError(f"Status inválido. Permitidos: {self.ALLOWED_STATUS}") 

        if "priority" in data and data["priority"] not in self.ALLOWED_PRIORITY:
            raise ValueError(f"Prioridade inválida. Permitidas: {self.ALLOWED_PRIORITY}") 

        if "due_date" in data:
            try:
                data["due_date"] = datetime.fromisoformat(data["due_date"].replace('Z', '+00:00'))
            except:
                raise ValueError("Formato de data inválido.")

        updated_task = task_repository.update_task(task_id, data)
        
        return task_schema(updated_task)
    
    def delete_task_service(self, task_id):
        if not task_repository.delete_task(task_id):
            raise ValueError("Tarefa não encontrada.")
        return True
