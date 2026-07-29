from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0
        self.speed_test_wait = WebDriverWait(self.driver, 120)
        self.twitter_wait = WebDriverWait(self.driver, 10)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        check_btn = self.speed_test_wait.until(
            ec.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button',
                )
            )
        )
        check_btn.click()
        down_xpath = '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3'
        up_xpath = '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3'

        # 2. Wait until the element no longer says "Finding optimal server..."
        self.speed_test_wait.until_not(
            ec.text_to_be_present_in_element(
                (By.XPATH, down_xpath), "Finding optimal server..."
            )
        )

        # 3. Safely capture the finalized numerical values
        down_speed = self.speed_test_wait.until(
            ec.visibility_of_element_located((By.XPATH, down_xpath))
        ).text
        up_speed = self.speed_test_wait.until(
            ec.visibility_of_element_located((By.XPATH, up_xpath))
        ).text

        return down_speed, up_speed

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        user_name_input = self.twitter_wait.until(
            ec.element_to_be_clickable((By.ID, "jf-input-username_or_email"))
        )
        user_name_input.clear()
        user_name_input.send_keys(TWITTER_EMAIL)

        continue_btn = self.twitter_wait.until(
            ec.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )

        sleep(2)
        # print(continue_btn)
        # continue_btn.click()
        continue_btn.send_keys(Keys.ENTER)
        sleep(3)
        password_input = self.twitter_wait.until(
            ec.element_to_be_clickable((By.ID, "jf-input-password"))
        )
        password_input.clear()
        password_input.send_keys(TWITTER_PASSWORD)


check_speed = InternetSpeedTwitterBot()
# down_speed, up_speed = check_speed.get_internet_speed()
check_speed.tweet_at_provider()
