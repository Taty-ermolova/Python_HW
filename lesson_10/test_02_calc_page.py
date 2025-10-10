import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.calc_page import CalcPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Этот тест проверяет правильность выполнения операций калькулятором.")
@allure.feature("Функциональность калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    calc_page = CalcPage(driver)

    @pytest.fixture
    def driver():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield driver
        driver.quit()

        with allure.step("Открыть страницу калькулятора"):
            calc_page.open()

        with allure.step("Ввести данные в поле ввода ожидания результата"):
            calc_page.input_field()

        with allure.step("Нажать кнопки"):
            calc_page.click_bottons()

        with allure.step("Дождаться результата"):
            count_result = calc_page.wait_result()

        with allure.step("Проверить результат"):
            assert count_result == '15'