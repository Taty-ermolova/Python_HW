from selenium.webdriver.common.by import By

class ShopPageCheckData:
    def __init__(self, driver):
        self.driver = driver

    def check_data(self):
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        assert total_price == "Total: $58.29"