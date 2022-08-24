
bot= 'x'
player='o'

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ',10: ' ',
         11: ' ',12: ' ',13: ' ',14: ' ',15: ' ',
         16: ' ',17: ' ',18: ' ',19: ' ',20: ' ',
         21: ' ',22: ' ',23: ' ',24: ' ',25: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10])
    print('-+-+-+-+-')
    print(board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15])
    print('-+-+-+-+-')
    print(board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20])
    print('-+-+-+-+-')
    print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25])
    print('-+-+-+-+-')




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

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10])
    print('-+-+-+-+-')
    print(board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15])
    print('-+-+-+-+-')
    print(board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20])
    print('-+-+-+-+-')
    print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25])
    print('-+-+-+-+-')


def spaceIsFree(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def checkWinner(board):
    if board[1] == board[2] == board[3] == board[4] == board[5] and (board[5] != ' '):
        return True
    elif (board[6] == board[7] == board[8] == board[9] == board[10] ) and (board[6] != ' '):
        return True
    elif board[11] == board[12] == board[13] == board[14] == board[15] and (board[15] != ' '):
        return True
    elif board[16] == board[17] == board[18] == board[19] == board[20] and (board[20] != ' '):
        return True
    elif board[21] == board[22] == board[23] == board[24] == board[25] and (board[25] != ' '):
        return True
    elif board[1] == board[6] == board[11] == board[16] == board[21] and (board[21] != ' '):
        return True
    elif board[2] == board[7] == board[12] == board[17] == board[22] and (board[22] != ' '):
        return True
    elif board[3] == board[8] == board[13] == board[18] == board[23] and (board[23] != ' '):
        return True
    elif board[4] == board[9] == board[14] == board[19] == board[24] and (board[24] != ' '):
        return True
    elif board[5] == board[10] == board[15] == board[20] == board[25] and (board[25] != ' '):
        return True
    elif board[1] == board[7] == board[13] == board[19] == board[25] and (board[25] != ' '):
        return True
    elif board[5] == board[9] == board[13] == board[17] == board[21] and (board[21] != ' '):
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
    if board[1] == board[2] == board[3] == board[4] == board[5] == mark:
        return True
    elif board[6] == board[7] == board[8] == board[9] == board[10] == mark:
        return True
    elif board[11] == board[12] == board[13] == board[14] == board[15] == mark:
        return True
    elif board[16] == board[17] == board[18] == board[19] == board[20] == mark:
        return True
    elif board[21] == board[22] == board[23] == board[24] == board[25] == mark:
        return True
    elif board[1] == board[6] == board[11] == board[16] == board[21] == mark:
        return True
    elif board[2] == board[7] == board[12] == board[17] == board[22] == mark:
        return True
    elif board[3] == board[8] == board[13] == board[18] == board[23] == mark:
        return True
    elif board[4] == board[9] == board[14] == board[19] == board[24] == mark:
        return True
    elif board[5] == board[10] == board[15] == board[20] == board[25] == mark:
        return True
    elif board[1] == board[7] == board[13] == board[19] == board[25] == mark:
        return True
    elif board[5] == board[9] == board[13] == board[17] == board[21] == mark:
        return True
    else:
        return False
def miniMax(board, depth,isMaximizing):
    if checkWhichMarkWon(bot,board):
        return 1
    elif checkWhichMarkWon(player,board):
        return -1
    elif checkDraw(board) or depth==5:
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
        




