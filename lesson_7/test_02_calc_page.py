import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_7.calc_page import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.input_field()
    calc_page.click_bottons()
    count_result = calc_page.wait_result()
    assert count_result == '15'
