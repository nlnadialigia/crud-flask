import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Task Test 01",
        "description": "Descrição da Task 01"
    }

    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 201
    response_body = response.json()
    assert "id" in response_body
    tasks.append(response_body['id'])
