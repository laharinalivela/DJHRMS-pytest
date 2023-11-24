# with token
import requests
import pytest
LOGOUT_URL = "https://dev-api.djhrm.com/api/auth/logout/"

def logout(token):
    payload = {token:token}
    print(token)
    response = requests.post (LOGOUT_URL, data=payload)
    return response
def test_logout_success():
    token = 'a1c033a4eae006415711ed8ecaec25110c976034'
    response = logout(token)
    print(response,111)
    assert response.status_code ==200, "Expected status code 200, but got {response.status_code}"

def test_logout_failure_invalid_token():
    token = 'a1c033a4eae006415711ed8ecaec25110c976034'
    response = logout (token)
    print(response)
    assert response.status_code == 200, "Login failed with an invalid token"
#

# without token

# import pytest
# import requests
#
# # Replace the following variables with your actual test data
# BASE_URL = "https://dev-api.djhrm.com/api/auth/logout/"
# @pytest.fixture
#
# def test_logout_no_token():
#     response = requests.post(BASE_URL)
#     assert response.status_code == 200
#     assert response.json()["detail"] == "Logged out successfully"
