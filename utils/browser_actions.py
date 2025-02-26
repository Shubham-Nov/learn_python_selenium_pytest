#browser_actions.py
from selenium import webdriver
import time #will be replaced with wait_until_element
from config.locators import get_locators
from selenium.webdriver.common.by import By

class BrowserActions:
    def __init__(self, driver):
        if driver.lower() == 'chrome':
            self.driver = webdriver.Chrome()

        if driver.lower() == 'firefox':
            self.driver = webdriver.Firefox()

        if driver.lower() == 'edge':
            self.driver = webdriver.Edge()

    base_url = None

    def open_browser(self, url = 'https://www.google.com/'):
        self.driver.get(url)
        self.driver.maximize_window()

    def search(self, input_txt, field='google_search'):
        """
        This method will be used by all classes to search on a particular field
        if provide none default to google/firefox/edge/.. search bar
        """
        global base_url
        if 'https' in input_txt:
            base_url = input_txt

        if field == 'google_search':
            self.driver.get(input_txt)
            time.sleep(20)

        else:
            self.driver.find_element(By.XPATH, get_locators(base_url, field)).send_keys(input_txt)
            time.sleep(6)

    def click(self, element):
        self.driver.find_element(By.XPATH, get_locators(base_url, element)).click()

    def get_title(self):
        return self.driver.title

    def close_browser(self):
        self.driver.quit()