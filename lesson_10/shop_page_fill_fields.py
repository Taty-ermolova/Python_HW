from selenium.webdriver.common.by import By

class ShopPageFillFields:
    def __init__(self, driver):
        """
            Инициализирует страницу магазина - личные данные.
            :param driver - экземпляр драйвера для браузера
        """
        self.driver = driver

    def fill_fields(self):
        """
            Заполняет поля личными данными.
            :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys("Татьяна")
        self.driver.find_element(By.ID, "last-name").send_keys("Ермолова")
        self.driver.find_element(By.ID, "postal-code").send_keys("394053")

    def continue_button(self):
        """
        Отправляет форму.
        :return: None
        """
        self.driver.find_element(By.ID, "continue").click()
