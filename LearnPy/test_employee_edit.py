import requests
import responses
import pytest
from decouple import config

@pytest.fixture
def login_user():
    login_url = "https://dev-api.djhrm.com/api/auth/login/"
    data = {'email': config('email1'), 'password': config('password1')}
    response = requests.post(login_url, data=data)
    return {'email': config('email1'), 'password': config('password1'), 'token': response.json()['key'], 'tenant_uid': response.json()['details']['tenant']['uid']}
def test_employee_edit(login_user):
    url = f"https://dev-api.djhrm.com/api/tenants/{login_user['tenant_uid']}/employee/edit/"
    print(url,111111111)
    edit_employee_data ={
        "phone_number" : "9368527410",
        "gender" : 2,
        "dob" : "2000-09-18",
        "blood_group" : "",
        "marital_status" : "",
        "alternative_email" : "divya@wmltech.com",
        "alternative_phone_number" : "7418520963"
    }
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.put(url, headers=headers, json=edit_employee_data)
    response.status_code == 200
    response = requests.put(url, edit_employee_data)
    print(response,1111111111)



