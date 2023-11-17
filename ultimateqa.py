from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




class UltimateQA:
    def __init__(self, driver):
        self.driver = driver

    def buttons(self):
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[1]/div[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[3]/div[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[4]/div[3]/a').click()

    def social_media(self):
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[1]/li/a').click()
        self.driver.back()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[2]/li/a').click()
        self.driver.back()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[3]/li/a').click()
        self.driver.back()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[4]/li/a').click()
        self.driver.back()
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[5]/div[1]/ul[5]/li/a').click()
        self.driver.back()

    def random_stuff(self):
        self.driver.find_element(By.XPATH, '//*[@id="lpwtoc_widget-2"]/div/div/div[1]/span/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="lpwtoc_widget-2"]/div/div/div[1]/span/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]').send_keys('Sauce Demo')
        self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_email_0"]').send_keys('saucedemo@gmail.com')
        self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_message_0"]').send_keys('Nice to meet you!')
        captcha = self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/div/p/span')
        result = eval(captcha.text)
        self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/div/p/input').send_keys(result)
        self.driver.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/button').click()

        self.driver.find_element(By.NAME, 'log').send_keys('Sauce Demo')
        self.driver.find_element(By.NAME, 'pwd').send_keys('secret_sauce')
        self.driver.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[7]/div[2]/div[2]/div[2]/form/p[4]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="backtoblog"]/a').click()


def main():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://ultimateqa.com/complicated-page')

    ultimate_qa = UltimateQA(driver)
    ultimate_qa.random_stuff()


if __name__ == "__main__":
    main()
