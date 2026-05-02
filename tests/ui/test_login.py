from pages.login_page import LoginPage
from utils.config import load_test_data
import requests

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

def test_login_and_validate_api_response(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["email"] == "Sincere@april.biz"