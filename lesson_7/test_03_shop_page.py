import pytest
from selenium import webdriver
from lesson_7.shop_page_authorization import ShopPageAuth
from lesson_7.shop_page_main import ShopPageMain
from lesson_7.shop_page_cart import ShopPageCart
from lesson_7.shop_page_fill_fields import ShopPageFillFields
from lesson_7.shop_page_check_data import ShopPageCheckData


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

def test_shop(driver):
    shop_page = ShopPageAuth(driver)
    shop_page.open()
    shop_page.authorization()
    shop_page = ShopPageMain(driver)
    shop_page.add_to_cart()
    shop_page.go_to_cart()
    shop_page = ShopPageCart(driver)
    shop_page.checkout_button()
    shop_page = ShopPageFillFields(driver)
    shop_page.fill_fields()
    shop_page.continue_button()
    shop_page = ShopPageCheckData(driver)
    shop_page.check_data()
