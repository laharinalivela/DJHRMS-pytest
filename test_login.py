import requests
import pytest

# Replace 'your_login_url' with the actual URL of your login page
LOGIN_URL = 'https://dev-api.djhrm.com/api/auth/login/'


def login(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post (LOGIN_URL, data=payload)
    return response
    token = response.json().get('key')
    assert token, "Token not found in the login response"
    return token
def test_login_success():
    email, password = 'lahari@wmltech.com', 'Wml@1234'
    token = login(email, password)
    assert token, "Token should not"

def test_login_success():
    email, password = 'lahari@wmltech.com', 'Wml@1234'
    response = login (email, password)
    assert response.status_code ==200, "Expected status code 200, but got {response.status_code}"



def test_login_failure_invalid_password():
    email, invalid_password ='lahari@wmltech.com', 'Wml@123'
    response = login (email, invalid_password)
    assert response.status_code == 400, "Login failed with an invalid password"


def test_login_failure_invalid_email():
    invalid_email, password ='lahari1@wmltech.com', 'Wml@1234'
    response = login (invalid_email, password)
    assert response.status_code == 400, "Login failed with an invalid email"
