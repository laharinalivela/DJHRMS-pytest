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


def test_all_employes(login_user):
    url = f"https://dev-api.djhrm.com/api/admin/tenants/{login_user['tenant_uid']}/all/employees/"
    headers = {'Authorization': f"Token {login_user['token']}"}
    response = requests.get (url, headers=headers, json=())
    assert response.status_code == 200, response.content
    employee_data = response.json()
    print (employee_data, 1111111)



