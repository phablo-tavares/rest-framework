import requests


endpoint = "http://localhost:8000/api/"

response = requests.get(
    endpoint, params={"abc": '123'}, json={"request data": 'this is my request data'})
print(response.json())
