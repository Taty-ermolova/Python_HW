from selenium.webdriver.common.by import By

class ShopPageAuth:
    def __init__(self, driver):
        """
            Инициализирует страницу магазина.
            :param driver: WebDriver - экземпляр драйвера для браузера
        """
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
            Открывает страницу.
            :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def authorization(self):
        """
            Заполняет форму авторизации.Отправляет форму авторизации.
            :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()