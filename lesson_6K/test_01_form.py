from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():

    edge_driver_path = r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")

    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")

    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")

    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    waiter = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary"))
    )
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
    submit_button.click()

    zip_code = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    fields = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id).value_of_css_property("background-color")
        assert field == "rgba(209, 231, 221, 1)"

    driver.quit()
