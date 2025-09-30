import requests


class ProjectYouGile:

    def __init__(self, url, mail, password, company) -> None:
        self.url = url
        self.token = self.get_token(mail, password, company)

    # Получить ключ авторизации
    def get_token(self, mail, password, company):
        creds = {
            "login": mail,
            "password": password,
            "companyid": company
        }
        resp = requests.post(self.url + 'auth/keys', json=creds)
        response_data = resp.json()
        print(response_data)
        # Извлекаем токен из ответа
        assert response_data.get('key')
        return response_data.get('key')

    # Получить список проектов компании
    def get_project_list(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()["content"]

    # Добавить проект:
    def create_project(self, title, user):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "title": title,
            "users": user
        }
        resp = requests.post(self.url + 'projects', headers=headers, json=project)
        return resp

    # Получить проект по id
    def get_project_with_id(self, project_id):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url + f'projects/{project_id}', headers=headers)
        return resp

    # Изменить проект
    def edit_project(self, project_id, new_title, new_user):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "title": new_title,
            "users": new_user
        }
        resp = requests.put(self.url + f'projects/{project_id}', headers=headers, json=project)
        return resp