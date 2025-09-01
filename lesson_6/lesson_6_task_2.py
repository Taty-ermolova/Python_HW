from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

search_bar = driver.find_element(By.ID, "newButtonName")
search_bar.send_keys("SkyPro")
blue_button = driver.find_element(By.ID, "updatingButton").click()
txt = driver.find_element(By.ID, "updatingButton").text

print(txt)

driver.quit()