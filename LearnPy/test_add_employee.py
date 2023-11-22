import requests
import responses
import pytest
from decouple import config

# Replace the following URL with the actual URL of the API endpoint
BASE_URL = "https://dev-api.djhrm.com/api/admin/tenants/2fa39c9d3f91/create/employee/"
@pytest.fixture
def login_user():
    login_url = "https://dev-api.djhrm.com/api/auth/login/"
    data = {'email': config('EMAIL'), 'password': config('PASSWORD')}
    response = requests.post(login_url, data=data)
    return {'email': config('EMAIL'), 'password': config('PASSWORD'), 'token': response.json()['key']}

def test_create_employee_success(login_user):

    employee_data = {
        "first_name": "sai",
        "last_name": "Krishna",
        "phone_number": "7418520963",
        "email": "sai@wmltech.com",
        "date_of_birth": "1999-06-22",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post (BASE_URL, headers=headers, json=employee_data)
    assert response.status_code == 201, response.content
    response = requests.post(BASE_URL,employee_data)

def test_existing_employee(login_user):
    employee_data = {
        "first_name": "sai",
        "last_name": "Krishna",
        "phone_number": "7418520963",
        "email": "sai@wmltech.com",
        "date_of_birth": "1999-06-22",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post (BASE_URL, headers=headers, json=employee_data)
    assert response.status_code == 400, response.content
    response = requests.post (BASE_URL, employee_data)

def test_add_employee_with_invalid_email(login_user):
    employee_data = {
        "first_name": "sai",
        "last_name": "Krishna",
        "phone_number": "7418520963",
        "email": "fdjvnsmca",
        "date_of_birth": "1999-06-22",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post (BASE_URL, headers=headers, json=employee_data)
    assert response.status_code == 400, response.content
    response = requests.post (BASE_URL, employee_data)
def test_add_employee_with_missing_required_field(login_user):
    employee_data = {
        "first_name": "",
        "last_name": "",
        "phone_number": "7418520963",
        "email": "sai@wmltech.com",
        "date_of_birth": "1999-06-22",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post (BASE_URL, headers=headers, json=employee_data)
    assert response.status_code == 400, response.content
    response = requests.post (BASE_URL, employee_data)
def test_add_employee_with_maximum_length_fields(login_user):
    employee_data = {
        "first_name": "sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai "
                      "sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai "
                      "sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai"
                      " sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai"
                      " sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai "
                      "sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai "
                      "sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai sai",
        "last_name": "Krishna",
        "phone_number": "7418520963",
        "email": "sai@wmltech.com",
        "date_of_birth": "1999-06-22",
        "gender": 1,
        "address": "123 Main Street",
        "city": "Madhapur",
        "state": 1,
        "country": 1,
        "pincode": "500081",
        "location": 1
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.post (BASE_URL, headers=headers, json=employee_data)
    assert response.status_code == 400, response.content
    response = requests.post (BASE_URL, employee_data)

