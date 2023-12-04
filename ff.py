import requests

url = 'http://127.0.0.1:5000'  # Замените на актуальный адрес сервера

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")