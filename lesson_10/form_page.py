from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        """
            Инициализирует страницу формы для заполнения.
            :param driver - экземпляр драйвера для браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.driver.maximize_window()
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self):
        """
        Открывает страницу.
        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    def fill_form(self):
        """
        Заполняет форму.
        :return: None
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def move_scroll(self):
        """
        Скроллит страницу вниз.
        :return: None
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def submit_form(self):
        """
        Отправляет форму.
        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, ".btn.btn-outline-primary"))).click()

    def check_zip_code_error(self) -> str:
        """
        Проверяет ошибку в поле zip-code.
        :return: str
        """
        zip_code = self.driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
        return zip_code

    def check_fields_success(self) -> str:
        """
        Проверяет успешное заполнение полей.
        :return: str
        """
        fields = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
        for field_id in fields:
            field = self.driver.find_element(By.ID, field_id).value_of_css_property("background-color")
        return field