#login_page.py
import time #will be replaced with wait_until_element

from config import locators
from selenium.webdriver.common.by import By
from utils.browser_actions import BrowserActions

class LoginPage(BrowserActions):
    def __init__(self, driver, url):
        self.driver = driver.driver
        self.username_input = (By.XPATH, locators.get_locators(url, 'username'))
        self.password_input =  (By.XPATH, locators.get_locators(url, 'password'))
        self.login_btn = (By.XPATH, locators.get_locators(url, 'login_btn'))

    def login(self, uname, passwd):
        self.driver.find_element(*self.username_input).send_keys(uname)
        self.driver.find_element(*self.password_input).send_keys(passwd)
        self.driver.find_element(*self.login_btn).click()
        time.sleep(7)