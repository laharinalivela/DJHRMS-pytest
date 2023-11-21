# import pytest
# import requests
#
# LOGIN_URL = 'https://dev-api.djhrm.com/api/auth/login/'
# BASE_URL1 = 'https://dev-api.djhrm.com/api/auth/password/change/'
#
# def login(email, password):
#     payload = {'email': email, 'password': password}
#     response = requests.post(LOGIN_URL, data=payload)
#
#     # Check if login was successful
#     assert response.status_code == 200, f"Login failed with status code {response.status_code}"
#
#     # Extract and return the token
#     token = response.json().get('key')
#     assert token, "Token not found in the login response"
#     return token
#
# def test_login_success():
#     email, password = 'lahari@wmltech.com', 'Wml@1234'
#     token = login(email, password)
#     assert token, "Token should not be empty or None"
#
# def change_password(Oldpassword, Newpassword, Confirmpassword, token):
#     headers = {"Authorization": f"Token {token}"}
#
#     payload = {'old_password': Oldpassword, 'new_password': Newpassword, 'confirm_password': Confirmpassword}
#     response = requests.post(BASE_URL1, headers=headers, data=payload)
#     return response
#
# def test_change_password_success():
#     # Perform login to get the token
#     email, password = 'lahari@wmltech.com', 'Wml@1234'
#     token = login(email, password)
#
#     print ("Token:", token)
#
#     # Use the obtained token for the change_password API call
#     Oldpassword, Newpassword, Confirmpassword = 'Wml@1234', 'Wml@12345', 'Wml@12345'
#     response = change_password(Oldpassword, Newpassword, Confirmpassword, token)
#
#     print(response.status_code)
#     print(response.text)
#
#     assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
import pytest
import requests
from decouple import config

url = "https://dev-api.djhrm.com/api/auth/password/change/"

@pytest.fixture

def login_user():

    login_url = "https://dev-api.djhrm.com/api/auth/login/"

    data = {'email': config('EMAIL'), 'password': config('PASSWORD')}

    response = requests.post(login_url, data=data)

    return {'email': config('EMAIL'), 'password': config('PASSWORD'), 'token': response.json()['key']}


def test_change_valid_credentials(login_user):

    data = {'old_password': config('OLD_PASSWORD'), 'new_password': config('NEW_PASSWORD'), 'confirm_password': config('CONFIRM_PASSWORD')}

    headers = {'Authorization': f"Token {login_user['token']}"}

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 200, response.content


def test_invalid_authentication():

    token = "wyudsbxawbclca"

    headers = {'Authorization': f"Token {token}"}

    response = requests.post(url, headers=headers)

    assert response.status_code == 403, response.content

