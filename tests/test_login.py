#test_login.py
from utils.browser_actions import BrowserActions
from pages.login_page import LoginPage
from config.settings import get_login_credentials

# test_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
test_url = 'https://www.amazon.in/'
task = BrowserActions('chrome')
task.open_browser()
task.search(test_url)
task.search('boy','amazon_search_bar')
task.click('amazon_search_bar_btn')
# task = LoginPage(task, test_url)
# task.login(get_login_credentials(test_url, 'username'), get_login_credentials(test_url, 'password'))
act_title = task.get_title()
task.close_browser()
exp_title = 'Amazon.in : boy'

assert act_title == exp_title