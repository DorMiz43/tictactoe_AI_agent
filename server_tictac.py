from crypt import methods
import requests
from flask import Flask , request , jsonify
from newOne import game,printBoard
app=Flask(__name__)#create an app instance
import json

from classTictoctoe import TictoctoeGame
game = TictoctoeGame()
@app.route('/',methods = ['GET','POST'])#route to handle the default home page)
def start_game():
    
    gameStarted = False
    if request.method == 'POST':
        
        d= request.get_json()
        print(d)
        position=int(d['position'])
        print(position)
        
        msg = game.insertLetter(position, 'o')
        if msg == True:
            msg = game.botMove()
        d = {'gameRunning':True,'Message':msg,'board':game.printBoard()}
        
        return jsonify(d)
    else:
        if gameStarted == False:
            gameStarted = True
            return jsonify({'gameRunning':True,
            'Message':'Welcome to TicTacToe Game Against The ARTIFICIAL INTELLIGENCE',
            'board':game.printBoard()})
        print("in the else")
        d = {'gameRunning':True}
        
        return jsonify(d)
        
if __name__=='__main__':
    app.run()#run the app in debug mode on port 5000

