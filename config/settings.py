#setting.py
def get_login_credentials(url):
    if 'https://opensource-demo.orangehrmlive.com/' in url:
        return {'username': 'Admin', 'password': 'admin123'}
    return None  # Return None if the URL does not match
