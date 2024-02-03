from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

not_found = 'Task não encontrada'


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

    return jsonify({'message': 'Nova tarefa criada com sucesso', 'id': new_task.id}), 201


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

    return jsonify({'message': not_found}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if not task:
        return jsonify({'message': not_found}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({'message': 'Task atualizada com sucesso', 'data': data})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({'message': not_found}), 404

    tasks.remove(task)

    return jsonify({'message': 'Task deletada com sucesso'})


if __name__ == "__main__":
    app.run(debug=True)
