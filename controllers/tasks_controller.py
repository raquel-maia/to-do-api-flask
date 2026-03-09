from flask import Blueprint, jsonify, request
from services.task_service import TaskService

task_routes = Blueprint('task', __name__)

task_service = TaskService()


@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    status_filter = request.args.get('status')
    
    tasks = task_service.list_all_tasks(status=status_filter)
    return jsonify(tasks), 200


@task_routes.route('/tasks', methods=['POST'])
def post_tasks():

    try:
        data = request.json
        task_created = task_service.create_task(data)

        return jsonify({
            "message": "Tarefa criada com sucesso!",
            "task": task_created
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        print(f"DEBUG: Ocorreu um erro inesperado: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500