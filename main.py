#main.py
from utils.browser_actions import BrowserActions
from pages.login_page import LoginPage
from config.settings import get_login_credentials

input_txt = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
task = BrowserActions()
task.open_browser('chrome')
task.search(input_txt)
task = LoginPage(task, input_txt)
task.login(get_login_credentials(input_txt)['username'], get_login_credentials(input_txt)['password'])
