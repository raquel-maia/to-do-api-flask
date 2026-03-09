from datetime import datetime, timezone
from repositories import task_repository
from schemas.task_schema import task_schema, tasks_schema


from datetime import datetime, timezone
from repositories import task_repository
from schemas.task_schema import task_schema, tasks_schema

class TaskService:

    ALLOWED_STATUS = ["pending", "in_progress", "completed", "cancelled"]
    ALLOWED_PRIORITY = ["low", "medium", "high"]

    def list_all_tasks(self, status=None):
        
        if status and status not in self.ALLOWED_STATUS:
            raise ValueError(f"Status '{status}' inválido. Permitidos: {self.ALLOWED_STATUS}")
        
        tasks = task_repository.list_tasks(status=status)
        return tasks_schema(tasks)

    def create_task(self, data):
    
        title = data.get("title", "").strip()
        status = data.get("status", "pending")
        priority = data.get("priority", "medium")
        due_date_str = data.get("due_date")
        
    
        if not title:
            raise ValueError("O título é obrigatório.")
        
        if len(title) < 3 or len(title) > 100:
            raise ValueError("O título deve ter entre 3 e 100 caracteres.")
        
        existing_task = task_repository.find_task_by_title(title)
        if existing_task:
            raise ValueError("Esse título já existe.")
            
        if status not in self.ALLOWED_STATUS:
            raise ValueError(f"Status inválido! Verifique os Status válidos: {self.ALLOWED_STATUS}")

        if priority not in self.ALLOWED_PRIORITY:
            raise ValueError(f"Prioridade inválida! Verifique as Prioridades válidas: {self.ALLOWED_PRIORITY}")

        try:
            due_date = datetime.fromisoformat(due_date_str.replace('Z', '+00:00'))
        except (ValueError, TypeError, AttributeError):
            raise ValueError("Data de vencimento inválida. Use o formato ISO (ex: 2026-03-09T15:00:00Z)")

        if due_date < datetime.now(timezone.utc):
            raise ValueError("A data de vencimento não pode estar no passado!")

        # Montagem do objeto
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