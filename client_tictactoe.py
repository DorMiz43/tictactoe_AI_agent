from crypt import methods
import requests
import json
# from newOne import *

address='http://127.0.0.1:5000/'
respondeFromServer = requests.get(address)
respondeFromServer = json.loads(respondeFromServer.text)

while respondeFromServer['gameRunning'] == True:
    if respondeFromServer['Message']!=True:
        print(respondeFromServer['Message'])
        if respondeFromServer['Message'] == 'Game Draw':
            print(respondeFromServer['board'])
            break
        elif respondeFromServer['Message'] == 'You Won':
            print(respondeFromServer['board'])
            break
        elif respondeFromServer['Message'] == 'Bot Won':
            print(respondeFromServer['board'])
            break
    print(respondeFromServer['board'])
    
    input_=input("Enter Your Move Please: ")
    # check if the input is an integer
    while not input_.isdigit():
        input_=input("enter valid num please: ")
    respondeFromServer = requests.post(address,json={'position':input_})
    #####
    respondeFromServer = json.loads(respondeFromServer.text)

