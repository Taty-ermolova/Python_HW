import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from lesson_7.form_page import FormPage


@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    yield driver
    driver.quit()

def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.move_scroll()
    form_page.submit_form()
    form_page.check_zip_code_error()
    form_page.check_fields_success()