import requests
from newOne import *

address='http://127.0.0.1:5000/'

response=requests.get(address)

print(response.text)
print("hello")
game()
