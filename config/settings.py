#setting.py
def get_login_credentials(url, key):
    if 'https://opensource-demo.orangehrmlive.com/' in url:
        credentials = {'username': 'Admin', 'password': 'admin123'}
        return credentials[key]
    return None  # Return None if the URL does not match
