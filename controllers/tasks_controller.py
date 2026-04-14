from flask import Blueprint, jsonify, request
from services.task_service import TaskService

task_routes = Blueprint('task', __name__)

task_service = TaskService()


@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    status_filter = request.args.get('status')
    
    tasks = task_service.list_all_tasks(status=status_filter)
    return jsonify(tasks), 200

@task_routes.route('/tasks/status/count', methods=['GET'])
def get_tasks_count_by_status():
    tasks = task_service.count_tasks_by_status()
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
    
@task_routes.route('/tasks/<task_id>', methods=['PUT'])

def update_tasks(task_id):
        try:
            data = request.json
            task_update = task_service.update_task_service(task_id, data)
            return jsonify({
                "message": "Tarefa atualizada com sucesso!",
                "task": task_update
            }), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:
            print(f"DEBUG: Ocorreu um erro inesperado: {e}")
            return jsonify({"error": "Erro interno do servidor"}), 500
        
@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task_service.delete_task_service(task_id)
        return jsonify({"message": "Tarefa deletada com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Erro interno do servidor"}), 500
    

