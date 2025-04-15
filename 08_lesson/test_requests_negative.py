import requests

base_url = 'https://ru.yougile.com/api-v2/'
token = 'insert_token'
headers = {'Authorization': f'Bearer {token}',
           "Content-Type": "application/json"}


# Создание проекта (post) - не передан headers with token.negative
def test_create_project_without_token():
    project = {
        "title": "{{$randomCurrencyName}}"
    }
    resp = requests.post(base_url + 'projects', json=project)
    assert resp.status_code == 401
    print(resp.text)


# Изменить проект (put) - неверный id.negative
def test_change_project_invalid_id():
    project = {
        "title": "{HW-6}"
    }
    project_id = "e3b81d1c-7440-4103-8a04"
    resp = requests.put(
        base_url + 'projects/' + project_id,
        json=project, headers=headers)
    assert resp.status_code == 401
    print(resp.text)


# Получить проект по ID (get)- неверный url.negative
def test_add_id_project_invalid_url():
    project_id = "6607d090-b020-4a68-830c-40e5b875a854"
    resp = requests.get(base_url + 'project' + project_id, headers=headers)
    assert resp.status_code == 401
    print(resp.text)
