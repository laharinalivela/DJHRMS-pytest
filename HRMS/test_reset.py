import requests
import pytest
login_url = "https://dev-api.djhrm.com/api/auth/login/"
reset_url = "https://dev-api.djhrm.com/api/auth/password/reset/"
def login(email):
    payload = {'email': email}
    response = requests.post(login_url, data=payload)
    assert response.status_code == 200, f"Login failed with status code {response.status_code}"
    token = response.json().get('key')
    assert token, "Token not found in the login response"
    return token
def test_restpassword():
    email = 'lahari@wmltech.com'
    response = login(email)
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
API_URL = "https://dev-api.djhrm.com/api/auth/password/reset/"
RESET_CONFIRM_URL = 'https://dev-api.djhrm.com/api/auth/password/reset/confirm/{uidb64}/{token}/'
@pytest.fixture
def valid_email():
    return "lahari@wmltech.com"
@pytest.fixture
def invalid_email():
    return "lahari11@wmltech.com"
def test_password_reset_with_valid_email(valid_email):
    response = requests.post(API_URL, json={"email": valid_email})
    assert response.status_code == 200, "valid mail"
    print(valid_email)
def test_password_reset_with_invalid_email(invalid_email):
    response = requests.post(API_URL, json={"email": invalid_email})
    assert response.status_code == 200, "Invalid email"
    print(test_password_reset_with_valid_email(invalid_email))
def test_password_reset_without_password(valid_email):
    response = requests.post(API_URL, json={"email": valid_email})
    assert response.status_code == 200
def test_reset_password_confirm(self, uidb64, token, password, confirm_password):
    url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)
    data = {'password': password, 'confirm_password': confirm_password}
    response = requests.post(url, json=data)
    return response
@pytest.fixture
def uidb64():
    return 'NA'
@pytest.fixture
def token():
    return 'bxyoou-bc5f13e7fa1a93cf0211f6349319236b'
def test_reset_password_confirm_successful(uidb64, token):
    reset_password_url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)
    print(f"Reset Password URL: {reset_password_url}")
    response = requests.post(reset_password_url, json={'password': 'Wml@1234', 'confirm_password': 'Wml@1234'})
    assert response.status_code == 200
