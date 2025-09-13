from selenium import webdriver
from selenium.webdriver.common.by import By

def test_shop():

    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_button.click()

    bolt_T_Shirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    bolt_T_Shirt_button.click()

    onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie_button.click()

    basket = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    basket.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Татьяна")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Ермолова")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("394053")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    sum = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_price = sum.text
    assert total_price == "Total: $58.29"
    driver.quit()
