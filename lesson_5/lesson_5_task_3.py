from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("1234")
sleep(6)

number_input.clear()
sleep(6)

number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
number_input.send_keys("5678")
sleep(6)

driver.quit()