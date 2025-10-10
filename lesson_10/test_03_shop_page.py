import pytest
from selenium import webdriver
from lesson_10.shop_page_authorization import ShopPageAuth
from lesson_10.shop_page_main import ShopPageMain
from lesson_10.shop_page_cart import ShopPageCart
from lesson_10.shop_page_fill_fields import ShopPageFillFields
from lesson_10.shop_page_check_data import ShopPageCheckData
import allure

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@allure.title("Тест магазина")
@allure.description("Этот тест проверяет функциональность добавления товара в корзину и оформления заказа.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    with allure.step("Авторизация пользователя"):
        auth_page = ShopPageAuth(driver)
        auth_page.open()
        auth_page.authorization()

    with allure.step("Добавление товара в корзину"):
        main_page = ShopPageMain(driver)
        main_page.add_to_cart()
        main_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = ShopPageCart(driver)
        cart_page.checkout_button()

    with allure.step("Заполнение полей"):
        fill_form_page = ShopPageFillFields(driver)
        fill_form_page.fill_fields()
        fill_form_page.continue_button()

    with allure.step("Проверка итоговой суммы"):
        check_page = ShopPageCheckData(driver)
        result_total_price = check_page.check_data()
        assert result_total_price == "Total: $58.29"