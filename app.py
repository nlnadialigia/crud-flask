from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()

    new_task = Task(
        id=task_id_control,
        title=data['title'],
        description=data.get('description', '')
    )

    tasks.append(new_task)
    task_id_control += 1

    return jsonify({'message': 'Nova tarefa criada com sucesso'})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return output


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({'message': 'Task não encontrada'}), 404


if __name__ == "__main__":
    app.run(debug=True)
