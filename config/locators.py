#locators.py
def get_locators(url, key):
    if 'demo.orangehrmlive.' in url:
        element = {'username': '//input[@name="username"]',
                    'password': '//input[@name="password"]',
                    'login_btn': '//button[@type="submit"]'
                    }
        return element[key]

    if 'amazon' in url:
        element = {'amazon_search_bar' : '//input[@id = "twotabsearchtextbox"]',
                   'amazon_search_bar_btn' : '//input[@id = "nav-search-submit-button"]'
                   }
        return element[key]