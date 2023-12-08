import requests

def registration_acc():
    url = 'http://178.253.23.8:5000/api/registration'
    # Пароли отправлять в хэшированном виде
    json_data = {'login': 'Андрей', 'pas1': '12345', 'pas2': '12345'}

    try:
        response = requests.post(url, json=json_data, headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        print(response.text)
        # CODE1 - удачно
        # CODE10 - Данный логин занят
        # CODE11 - длина пароля меньше минимума
        # CODE12 - пароли не совпадают

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")


def login_acc():
    url = ('http://178.253.23.8:5000/api/login')
    # Пароли отправлять в хэшированном виде
    json_data = {'login': 'Андрей', 'pas': '12345'}

    try:
        response = requests.post(url, json=json_data, headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        print(response.text)
        # <ID> - удачно
        # CODE13 - Данного логина нет
        # CODE14 - пароль не верен

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")


def dd():
    url = ('http://127.0.0.1:3000/api/dd')
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.json())
        # <ID> - удачно
        # CODE13 - Данного логина нет
        # CODE14 - пароль не верен

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")

# registration_acc()
# login_acc()
dd()


# 200
# 300
#
#

# if response.status_code == 200:
#     # print(response.json())
#     response.json()
#
# else:
#     print(f"Error: {response.status_code}")