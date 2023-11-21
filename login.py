def login(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post(LOGIN_URL, data=payload)
    return response.status_code == 200