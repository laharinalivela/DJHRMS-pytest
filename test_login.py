import requests
import pytest
from decouple import config

LOGIN_URL = 'https://dev-api.djhrm.com/api/auth/login/'


def login(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post(LOGIN_URL, data=payload)
    return response
    token = response.json().get('key')
    assert token, "Token not found in the login response"
    return token

# def test_login_success():
#     email, password = config('email'), config('password')
#     token = login(email, password)
#     print(token,1111111111)
#
#     assert token, "Token should not"

def test_login_success():
    email, password = config('email'), config('password')
    response = login (email, password)
    assert response.status_code ==200, "Expected status code 200, but got {response.status_code}"
    assert 'key' in response.json()
    print(response.json())



def test_login_failure_invalid_password():
    email, invalid_password =config('email'), config('invalid_password')
    response = login (email, invalid_password)
    assert response.status_code == 400, "Login failed with an invalid password"


def test_login_failure_invalid_email():
    invalid_email, password =config('invalid_email'), config('password')
    response = login (invalid_email, password)
    assert response.status_code == 400, "Login failed with an invalid email"
def test_login_failure_invalid_email_and_invalid_password():
    invalid_email, invalid_password = config('invalid_email'), config('invalid_password')
    response = login (invalid_email,invalid_password)
    assert response.status_code == 400, "ligin failed with an invalid email and invalid password"
