from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://ultimateqa.com/complicated-page')


def buttons():
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[3]/a').click()


def social_media():
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[1]/li/a').click()
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[2]/li/a').click()
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[3]/li/a').click()
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[4]/li/a').click()
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[5]/li/a').click()
    driver.back()


if __name__ == "__main__":
    buttons()
    social_media()
