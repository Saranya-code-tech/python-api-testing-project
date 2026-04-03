import requests

from utils.api_client import post_request
from utils.config import base_url

def test_create_post_request():
    payload = {
        "userId": 11,
        "title": "new title",
        "body": "new body"
      }
    response = post_request("/posts", payload)
    data = response.json()
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 2
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert data["body"] == payload["body"]
    assert "id" in data