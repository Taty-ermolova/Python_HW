from project_YouGile import ProjectYouGile

def test_create_project_positive():
    new_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                     mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")

    response_create_project = new_project.create_project(title='Test company', user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert response_create_project.status_code == '201'

def test_create_project_negative():
    bad_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                     mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    response_create_project = bad_project.create_project(title='', user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert response_create_project.status_code == '400'
    assert response_create_project.message == "title should not be empty"

def test_get_project_with_id_positive():
    get_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                     mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    response_get_project_with_id = get_project.create_project(title='Second company', user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    project_id = response_get_project_with_id.json()['id']
    answer_get_project_with_id = get_project.get_project_with_id(project_id)

    assert answer_get_project_with_id.status_code == '200'
    assert answer_get_project_with_id.json()['title'] == 'Second company'
    assert answer_get_project_with_id.json()['users'] == '"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"'

def test_get_project_with_id_negative():
    non_existent_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                                 mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    response_get_project_with_id = non_existent_project.get_project_with_id("1000000000")

    assert response_get_project_with_id.status_code == '404'

def test_edit_project_positive():
    edit_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                                 mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    response_new_project = edit_project.create_project(title='Third company', user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    project_id = response_new_project.json()['id']
    response_edit_project = edit_project.edit_project(project_id, new_title='Fourth company', new_user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')
    response_get_project = edit_project.get_project_with_id(project_id)

    assert response_get_project.status_code == '200'
    assert response_get_project.json()['title'] == 'Fourth company'

def test_edit_project_negative():
    non_existent_edit_project = ProjectYouGile(url='https://ru.yougile.com/api-v2/',
                                 mail='taty.ermolova@gmail.com', password='Taty15362478!', company="b64c5019-ccfa-48fc-9071-5f6b81bdf126")
    response_edit_project = non_existent_edit_project.edit_project(project_id='344556677899', new_title='Fourth company', new_user='"10883214-ed6f-4370-a289-e56a53bf7f1d": "worker"')

    assert response_edit_project.status_code == '404'
    assert response_edit_project.message == "Проект не найден"
    assert response_edit_project.error == "Not Found"
