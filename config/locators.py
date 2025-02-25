#locators.py
def get_locators(url):
    if 'https://opensource-demo.orangehrmlive.com' in url:
       return {'username': '//input[@name="username"]', 'password': '//input[@name="password"]', 'login_btn': '//button[@type="submit"]'}