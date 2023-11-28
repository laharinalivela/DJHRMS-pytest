import requests
import pytest

FORGOT_PASSWORD_URL = 'https://dev-api.djhrm.com/api/auth/password/reset/'
RESET_CONFIRM_URL = 'https://dev-api.djhrm.com/api/auth/password/reset/confirm/{uidb64}/{token}/'


def forgot_password(email):
    response = requests.post(FORGOT_PASSWORD_URL, json={'email': email})
    return response


def test_forgot_password_successful():
    email = 'lahari@wmltech.com'

    response = forgot_password(email)

    assert response.status_code == 200
    assert response.json() is not None


def reset_password_confirm(uidb64, token, password, confirm_password):
    url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)
    data = {'password': password, 'confirm_password': confirm_password}
    response = requests.post(url, json=data)
    return response


@pytest.fixture
def uidb64():
    return 'NA'


@pytest.fixture
def token():
    return 'byc5ik-f3f9b25a489a77550714c7efcd73727b'


def test_reset_password_confirm_successful(uidb64, token):
    reset_password_url = RESET_CONFIRM_URL.format(uidb64=uidb64, token=token)

    print(f"Reset Password URL: {reset_password_url}")
    response = requests.post(reset_password_url, json={'password': 'Wml@1234', 'confirm_password': 'Wml@1234'})
    assert response.status_code == 200