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
        title=data['title'],
        description=data.get('description', ''),
        id=task_id_control
    )

    tasks.append(new_task)

    task_id_control += 1

    print(tasks)

    return jsonify({'message': 'Nova tarefa criada com sucesso'})


if __name__ == "__main__":
    app.run(debug=True)
