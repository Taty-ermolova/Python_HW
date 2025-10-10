from selenium.webdriver.common.by import By

class ShopPageCart:
    def __init__(self, driver):
        """
            Инициализирует страницу магазина - корзина.
            :param driver - экземпляр драйвера для браузера
        """
        self.driver = driver

    def checkout_button(self):
        """
            Нажатие на кнопку Проверить.
            :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()