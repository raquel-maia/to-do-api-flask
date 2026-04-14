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
        status = data.get("status", "pending")
        priority = data.get("priority", "medium")

        title = self.validate_title(data.get("title", ""))

        if status not in self.ALLOWED_STATUS:
            raise ValueError(f"Status inválido. Permitidos: {self.ALLOWED_STATUS}")

        if priority not in self.ALLOWED_PRIORITY:
            raise ValueError(f"Prioridade inválida. Permitidas: {self.ALLOWED_PRIORITY}")

        due_date_str = data.get("due_date")
        due_date = self._validate_due_date(due_date_str)

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

        # Regra: tarefa concluída
        if existing_task["status"] == "completed":
            allowed_fields = ["description", "title"]

            for field in data:
                if field not in allowed_fields:
                    raise ValueError("Tarefas concluídas só podem alterar título ou descrição.")

        # Segurança: campos permitidos
        allowed_update_fields = ["title", "description", "status", "priority", "due_date"]

        for field in data:
            if field not in allowed_update_fields:
                raise ValueError(f"Campo '{field}' não permitido.")

        # Validação de título
        if "title" in data:
            data["title"] = self.validate_title(data["title"], task_id=task_id)

        # Validação de status
        if "status" in data and data["status"] not in self.ALLOWED_STATUS:
            raise ValueError(f"Status inválido. Permitidos: {self.ALLOWED_STATUS}")

        # Regra extra: não permitir voltar de completed
        if existing_task["status"] == "completed" and "status" in data:
            raise ValueError("Não é permitido alterar o status de uma tarefa concluída.")

        # Validação de prioridade
        if "priority" in data and data["priority"] not in self.ALLOWED_PRIORITY:
            raise ValueError(f"Prioridade inválida. Permitidas: {self.ALLOWED_PRIORITY}")

        # Validação de data
        if "due_date" in data:
            data["due_date"] = self._validate_due_date(data["due_date"])

        updated_task = task_repository.update_task(task_id, data)

        return task_schema(updated_task)

    def delete_task_service(self, task_id):
        if not task_repository.delete_task(task_id):
            raise ValueError("Tarefa não encontrada.")
        return True

    def count_tasks_by_status(self):
        return task_repository.count_task_by_status()

    def _validate_due_date(self, due_date_str):

        if not due_date_str:
            return None

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            due_date = due_date.replace(tzinfo=timezone.utc)
        except ValueError:
            raise ValueError("Formato de data inválido. Use YYYY-MM-DD.")

        today = datetime.now(timezone.utc)

        if due_date < today:
            raise ValueError("A data de vencimento não pode ser no passado.")

        return due_date

    def validate_title(self, title, task_id=None):
        title = title.strip()

        if not title:
            raise ValueError("O título é obrigatório.")

        if len(title) < 3 or len(title) > 100:
            raise ValueError("O título deve ter entre 3 e 100 caracteres.")

        existing_task = task_repository.find_task_by_title(title)

        if existing_task and (not task_id or str(existing_task["_id"]) != str(task_id)):
            raise ValueError("Esse título já existe.")

        return title