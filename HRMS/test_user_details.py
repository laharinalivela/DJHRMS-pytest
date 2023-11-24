import requests
import responses
import pytest
from decouple import config

@pytest.fixture
def login_user():
    login_url = "https://dev-api.djhrm.com/api/auth/login/"
    data = {'email': config('EMAIL'), 'password': config('PASSWORD')}
    response = requests.post(login_url, data=data)
    return {'email': config('EMAIL'), 'password': config('PASSWORD'), 'token': response.json()['key']}
def test_user_details(login_user):
    url = "https://dev-api.djhrm.com/api/auth/user/"
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.get (url, headers=headers, json=())
    assert response.status_code == 200, response.content
    userdata = response.json()
    print (userdata,1111111)


