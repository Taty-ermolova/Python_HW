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
    auth_page = ShopPageAuth(driver)
    auth_page.open()
    auth_page.authorization()

    main_page = ShopPageMain(driver)
    main_page.add_to_cart()
    main_page.go_to_cart()

    cart_page = ShopPageCart(driver)
    cart_page.checkout_button()

    fill_form_page = ShopPageFillFields(driver)
    fill_form_page.fill_fields()
    fill_form_page.continue_button()

    check_page = ShopPageCheckData(driver)
    result_total_price = check_page.check_data()
    assert result_total_price == "Total: $58.29"