from pages.login_page import LoginPage
from utils.config import load_test_data

def test_valid_login(driver):
    data = load_test_data()
    user = data["valid_user"]

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(user["username"], user["password"])

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    data = load_test_data()
    user = data["invalid_user"]

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(user["username"], user["password"])

    assert "Sorry, this user has been locked out" in login_page.get_error_message()