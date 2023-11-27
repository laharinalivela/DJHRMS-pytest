import requests
import responses
import pytest
from decouple import config

@pytest.fixture
def login_user():
    login_url = "https://dev-api.djhrm.com/api/auth/login/"
    data = {'email': config('email'), 'password': config('password')}
    response = requests.post(login_url, data=data)
    return {'email': config('email'), 'password': config('password'), 'token': response.json()['key'], 'tenant_uid': response.json()['details']['tenant']['uid']}
def test_employee_edit(login_user):
    url = f"https://dev-api.djhrm.com/api/admin/tenants/{login_user['tenant_uid']}/all/employees/20/"
    edit_employee_data ={
            "phone_number": "9638520741",
            "gender": 1,
            "dob": "2023-11-24",
            "is_active": "true",
            "experience": 3,
            "designation": "",
            "reporting_manager": 1,
            "secondary_reporting_manager": 3,
            "blood_group": "",
            "marital_status": "",
            "alternative_email": "lahari12@wmltech.com",
            "alternative_phone_number": "string",
            "number": 9223372036,
            "date_of_joining": "2023-11-24",
            "type": "",
            "location": 1
    }

    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.put(url, headers=headers, json=edit_employee_data)
    response.status_code == 200
    print(response,11111111)




