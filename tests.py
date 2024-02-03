import requests

BASE_URL = 'http://127.0.0.1:5000/tasks'
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Task Test 01",
        "description": "Descrição da Task 01"
    }

    response = requests.post(f'{BASE_URL}', json=new_task_data)
    assert response.status_code == 201
    response_body = response.json()
    assert "id" in response_body
    tasks.append(response_body['id'])


def test_get_tasks():
    response = requests.get(f'{BASE_URL}')
    assert response.status_code == 200
    assert 'tasks' in response.json()
    assert 'total_tasks' in response.json()


def test_get_task_by_id():
    if tasks:
        task = tasks[0]
        response = requests.get(f'{BASE_URL}/{task}')
        assert response.status_code == 200
        body = response.json()
        assert task == body['id']


def test_update_task():
    if tasks:
        task = tasks[0]
        payload = {
            "title": "Task 01",
            "description": "Atualização Task 01",
            "completed": False
        }
        response = requests.put(f'{BASE_URL}/{task}', json=payload)
        assert response.status_code == 200
        body = response.json()
        assert body['data'] == payload


def test_delete_task():
    if tasks:
        task = tasks[0]
        response = requests.delete(f'{BASE_URL}/{task}')
        assert response.status_code == 200

        response = requests.get(f'{BASE_URL}/{task}')
        assert response.status_code == 404
