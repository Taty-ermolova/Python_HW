import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.form_page import FormPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Отправка тестовой формы")
@allure.description("Этот тест проверяет процесс отправки формы и подтверждает успешное заполнение полей.")
@allure.feature("Функция отправки формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_form(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open()

    with allure.step("Заполнить форму"):
        form_page.fill_form()

    with allure.step("Прокрутить до кнопки отправки"):
        form_page.move_scroll()

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Проверить цвет незаполненного поля Zip code"):
        result_zip_code = form_page.check_zip_code_error()
        assert result_zip_code == "rgba(248, 215, 218, 1)", "Цвет поля красный"

    with allure.step("Проверить цвет корректно заполненных полей"):
        result_field = form_page.check_fields_success()
        assert result_field == "rgba(209, 231, 221, 1)", "Цвет полей зеленый"