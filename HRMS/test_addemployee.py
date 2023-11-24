# without tenant id
import requests
import responses
import pytest

from decouple import config
@pytest.fixture
def login_user():
    login_url = "https://dev-api.djhrm.com/api/auth/login/"
    data = {'email': config('EMAIL'), 'password': config('PASSWORD')}
    response = requests.post(login_url, data=data)
    return {'email': config('EMAIL'), 'password': config('PASSWORD'), 'token': response.json()['key'], 'tenant_uid': response.json()['details']['tenant']['uid']}

def test_create_employee_success(login_user):
    BASE_URL = f"https://dev-api.djhrm.com/api/admin/tenants/{login_user['tenant_uid']}/create/employee/"
    print(BASE_URL,1111)
    employee_data = {
        "first_name": "sai",
        "last_name": "Krishna",
        "phone_number": "7418520963",
        "email": "krishna@wmltech.com",
        "date_of_birth": "1999-06-23",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post(BASE_URL , headers=headers, json=employee_data)
    assert response.status_code == 201, response.content
    response = requests.post (BASE_URL, employee_data)
    