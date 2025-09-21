import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_7.form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.move_scroll()
    form_page.submit_form()
    result_zip_code = form_page.check_zip_code_error()
    assert result_zip_code == "rgba(248, 215, 218, 1)"
    result_field = form_page.check_fields_success()
    assert result_field == "rgba(209, 231, 221, 1)"