from flask import Flask
from controllers.tasks_controller import task_routes

app = Flask(__name__)

app.register_blueprint(task_routes)

if __name__ == "__main__":
    app.run(debug=True, port=8080)