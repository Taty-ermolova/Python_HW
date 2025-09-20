from selenium.webdriver.common.by import By

class ShopPageAuth:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()