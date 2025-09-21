from selenium.webdriver.common.by import By

class ShopPageCart:
    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        self.driver.find_element(By.ID, "checkout").click()
