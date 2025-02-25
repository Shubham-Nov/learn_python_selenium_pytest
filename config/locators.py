#locators.py
def get_locators(url, key):
    if 'https://opensource-demo.orangehrmlive.com' in url:
        locators = {'username': '//input[@name="username"]',
                    'password': '//input[@name="password"]',
                    'login_btn': '//button[@type="submit"]'
                    }
        return locators[key]