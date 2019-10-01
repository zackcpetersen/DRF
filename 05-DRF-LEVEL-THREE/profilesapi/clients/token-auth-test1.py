import requests


def client():
    token_h = 'Token 03ce91629b1ad7ec4bda1c3da23b2838b6cca3c5'
    # credentials = {'username': 'zackcpetersen', 'password': ''}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    headers = {'Authorization': token_h}

    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
