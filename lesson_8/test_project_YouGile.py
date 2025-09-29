from lesson_8.project_YouGile import ProjectYouGile

def test_create_project_positive():
    new_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                     'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")

    new_project.create_project('Test company', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert new_project.statusCode == '201'

def test_create_project_negative():
    bad_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                     'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    bad_project.create_project('', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert bad_project.statusCode == '400'
    assert bad_project.message == "title should not be empty"

def test_get_project_with_id_positive():
    get_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                     'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    get_project.create_project('Second company', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    project_id = get_project.json()['id']
    get_project.get_project_with_id(project_id)

    assert get_project.statusCode == '200'
    assert get_project.json()['title'] == 'Second company'
    assert get_project.json()['users'] == '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"'

def test_get_project_with_id_negative():
    non_existent_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                                 'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    non_existent_project.get_project_with_id("1000000000")

    assert non_existent_project.statusCode == '404'


def test_edit_project_positive():
    edit_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                                 'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    edit_project.create_project('Third company', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    project_id = edit_project.json()['id']
    edit_project.edit_project(project_id, 'Fourth company', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    edit_project.get_project_with_id(project_id)

    assert edit_project.statusCode == '200'
    assert edit_project.json()['title'] == 'Fourth company'

def test_edit_project_negative():
    non_existent_edit_project = ProjectYouGile('https://ru.yougile.com/api-v2/',
                                 'taty.ermolova@gmail.com', 'Taty15362478!', "b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    non_existent_edit_project.edit_project('344556677899', 'Fourth company', '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert non_existent_edit_project.statusCode == '404'
    assert non_existent_edit_project.message == "Проект не найден"
    assert non_existent_edit_project.error == "Not Found"
