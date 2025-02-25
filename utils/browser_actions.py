#browser_actions.py
from selenium import webdriver
import time #will be replaced with wait_until_element

class BrowserActions:
    def __init__(self):
        self.driver = None

    def open_browser(self, driver):
        if driver.lower() == 'chrome':
            self.driver = webdriver.Chrome()
            self.driver.get('https://www.google.com/')
            self.driver.maximize_window()

        if driver.lower() == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.get('https://www.google.com/')
            self.driver.maximize_window()

        if driver.lower() == 'edge':
            self.driver = webdriver.Edge()
            self.driver.get('https://www.google.com/')
            self.driver.maximize_window()

    def search(self, input_txt):
        self.driver.get(input_txt)
        time.sleep(8)

    def get_title(self):
        return self.driver.title