from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_path = os.environ.get("CHROME_PATH")
        self.driver = webdriver.Chrome(executable_path=self.chrome_path)
        self.promised_down = 150
        self.promised_up = 10
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(40)
        download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.download_speed = float(download_speed.text)
        upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.upload_speed = float(upload_speed.text)

    def tweet_at_provider(self):
        if self.download_speed < self.promised_down or self.upload_speed < self.promised_up:
            ########################## LOG IN ##########################
            self.driver.get("https://twitter.com/login")
            time.sleep(5)
            username = self.driver.find_element_by_name("session[username_or_email]")
            username.send_keys(TWITTER_EMAIL)
            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            ########################## Tweeting ##########################
            tweet_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
            tweet_bar.send_keys(f"Hey @Internet_Provider, why is my internet speed {self.download_speed}-down/{self.upload_speed}-up when i pay for {self.promised_down}-down/{self.promised_up}-up")
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()
            self.driver.quit()


