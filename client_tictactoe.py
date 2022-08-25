import requests

address='http://127.0.0.1:5000/start'

response=requests.get(address)

print(response.text)