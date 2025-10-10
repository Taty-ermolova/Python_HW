from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.
        :param driver - экземпляр драйвера для браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.driver.maximize_window()

    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def input_field(self) -> None:
        """
        Вводит значение в поле задержки.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def click_buttons(self) -> None:
        """
        Нажимает кнопки "7", "+", "8" и "=" на калькуляторе.
        :return: None
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_result(self) -> str:
        """
        Ожидает и возвращает результат вычисления.
        :return: str - результат вычисления
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
        )
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return result