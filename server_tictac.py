from flask import Flask
from newOne import game
app=Flask(__name__)#create an app instance

# @app.route('/home',methods=['GET','POST'])#route to handle the default home page
# def home():
#     return '<h1>Home</h1>'

# @app.route('/')#
# def hello_world():
#     return f"hey, and welcome to our TicTacToeGame"

@app.route('/')#route to handle the default home page)
def start_game():
    # print("startgame")
    return "start_game"

    # return game()


if __name__=='__main__':
    app.run()#run the app in debug mode on port 5000

