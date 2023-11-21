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
    # Make a request to the password reset API with a valid email
    response = requests.post(API_URL, json={"email": valid_email})

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200, "valid mail"
    print(valid_email)
    # Add additional assertions based on the API response content, if needed
    # For example, you might check if the response contains a success message

def test_password_reset_with_invalid_email(invalid_email):
    # Make a request to the password reset API with an invalid email
    response = requests.post(API_URL, json={"email": invalid_email})

    # Check that the response status code is 400 (Bad Request) or another appropriate code
    assert response.status_code == 200, "Invalid email"
    print(test_password_reset_with_valid_email(invalid_email))
#
#     # Add additional assertions based on the API response content, if needed
#     # For example, you might check if the response contains an error message
#
def test_password_reset_without_password(valid_email):
    # Make a request to the password reset API without providing a password
    response = requests.post(API_URL, json={"email": valid_email})
#
#     # Check that the response status code is 400 (Bad Request) or another appropriate code
    assert response.status_code == 200

def test_reset_password_confirm(self, uidb64, token, password, confirm_password):
    url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)
    data = {'password': password, 'confirm_password': confirm_password}
    response = requests.post(url, json=data)
    return response


@pytest.fixture
def uidb64():
    # You can generate or provide a sample uidb64 for testing
    return 'NA'

@pytest.fixture
def token():
    # You can generate or provide a sample token for testing
    return 'bxyoou-bc5f13e7fa1a93cf0211f6349319236b'


def test_reset_password_confirm_successful(uidb64, token):
    # Get the reset password URL
    reset_password_url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)

    # Print or use the reset password URL
    print(f"Reset Password URL: {reset_password_url}")

    # Mock the HTTP request to the reset password URL (assuming it returns a success response)
    response = requests.post(reset_password_url, json={'password': 'Wml@1234', 'confirm_password': 'Wml@1234'})
    assert response.status_code == 200
