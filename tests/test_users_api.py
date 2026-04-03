import pytest
from utils.api_client import get_request

@pytest.fixture
def users_response():
    return get_request("/users")

@pytest.fixture
def invalid_endpoint():
    return get_request("/invalid")

def test_get_users(users_response):
    response = users_response
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)


def test_user_count(users_response):
    response = users_response
    data = response.json()
    assert data is not None
    data_len = len(data)
    assert (data_len == 10)
    first_user = data[0]
    assert "name" in first_user
    assert "email" in first_user

def test_invalid_endpoint(invalid_endpoint):
    response = invalid_endpoint
    data = response.json()
    assert response.status_code == 404

def test_first_user(users_response):
    response = users_response
    data = response.json()
    first_user = data[0]
    assert first_user["id"] == 1
    assert "address" in first_user
    assert isinstance(first_user["address"], dict)
    assert "city" in first_user["address"]
    assert first_user["address"]["city"] is not None
