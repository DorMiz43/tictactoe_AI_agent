
bot= 'x'
player='o'

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3]  )
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6]  )
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9]  )
    print()




def spaceIsFree(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def insertLetter(letter, board, position):
    if spaceIsFree(board, position):
        board[position] = letter
        printBoard(board) # print the board after each move
        if checkDraw(board):
            print('Draw')
            exit()
        if checkWinner(board):
            if letter==bot:
                print('Bot wins')
                exit()
            else:
                print('Player 2 wins')
                exit()

            
    else:
        print('Space is already taken')
        printBoard(board)
        position=int(input('Choose a different position:\t'))
        insertLetter(letter, board, position)

def checkWinner(board):
    if board[1] == board[2] == board[3] and (board[1] != ' '):
        return True
    elif board[4] == board[5] == board[6] and (board[4] != ' '):
        return True
    elif board[7] == board[8] == board[9] and (board[7] != ' '):
        return True
    elif board[1] == board[4] == board[7] and (board[1] != ' '):
        return True
    elif board[2] == board[5] == board[8] and (board[2] != ' '):
        return True
    elif board[3] == board[6] == board[9] and (board[3] != ' '):
        return True
    elif board[1] == board[5] == board[9] and (board[1] != ' '):
        return True
    elif board[3] == board[5] == board[7] and (board[3] != ' '):
        return True
    else:
        return False

def checkDraw(board):
    for k in board.keys():
        if board[k] == ' ':
            return False
    return True


def insertLetter(letter, board, position):
    if spaceIsFree(board, position):
        board[position] = letter
        printBoard(board) # print the board after each move
        if checkDraw(board):
            print('Draw')
            exit()
        if checkWinner(board):
            if letter==bot:
                print('Bot wins')
                exit()
            else:
                print('Player 2 wins')
                exit()
            
    else:
        print('Space is already taken')
        printBoard(board)
        position=int(input('Choose a different position:\t'))
        insertLetter(letter, board, position)

def playerMove(board):
    printBoard(board)
    position = int(input('Choose a position for O:\t'))
    insertLetter(player, board, position)

def botMove():
    bestScore=-800
    bestMove=0
    for key in board.keys():
        if board[key]==' ':
            board[key]=bot
            score=miniMax(board,0, False)
            board[key]=' '
            if score>bestScore:
                bestScore=score
                bestMove=key
    insertLetter(bot, board, bestMove)

def checkWhichMarkWon(mark,board):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
        
    else:
        return False
def miniMax(board, depth,isMaximizing):
    
    

    if checkWhichMarkWon(bot,board):
        return 1
    elif checkWhichMarkWon(player,board):
        return -1
    elif checkDraw(board):
        return 0
    if isMaximizing:
        bestScore=-800
        
        for key in board.keys():
            if board[key]==' ':
                board[key]=bot
                score=miniMax(board,depth+1, False)
                board[key]=' '
                
                if score>bestScore:
                    bestScore=score

        return bestScore
                    
    else:
        bestScore=800
        print(2111111111111)
        for key in board.keys():
            if board[key]==' ':
                board[key]=player
                score=miniMax(board, depth+1, True)
                board[key]=' '
                if score<bestScore:
                    bestScore=score
        return bestScore

if __name__ == '__main__':
        
    while not checkWinner(board):
        playerMove(board)
        botMove()
        




