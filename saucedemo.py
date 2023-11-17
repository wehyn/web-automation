from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("secret")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("1600")
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()

    print("Order done")



main()