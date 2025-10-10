from selenium.webdriver.common.by import By

class ShopPageCheckData:
    def __init__(self, driver):
        """
            Инициализирует страницу магазина - оформление заказа.
            :param driver - экземпляр драйвера для браузера
        """
        self.driver = driver

    def check_data(self):
        """
        Проверяет итоговую сумму заказа.
        :return: str
        """
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_price
