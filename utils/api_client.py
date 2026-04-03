import requests
from utils.config import base_url

def get_request(endpoint):
    response = requests.get(base_url + endpoint)
    return response

def post_request(endpoint, payload):
    return requests.post(base_url + endpoint, json=payload)