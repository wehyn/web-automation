from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("standard_user")
        self.driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("secret")
        self.driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("1600")
        self.driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="finish"]').click()

        print("Shopping is done.")


@pytest.fixture
def setup():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    return driver


def test_shopping_flow(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    shopping_cart_page = ShoppingCartPage(driver)
    shopping_cart_page.checkout()
