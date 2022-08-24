from turtle import position


board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ',
         11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
         16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
         21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ',}

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
    if board[1] == board[2] == board[3] == board[4] == board[5] == ' ':
        return True
    elif board[6] == board[7] == board[8] == board[9] == board[10] == ' ':
        return True
    elif board[11] == board[12] == board[13] == board[14] == board[15] == ' ':
        return True
    elif board[16] == board[17] == board[18] == board[19] == board[20] == ' ':
        return True
    elif board[21] == board[22] == board[23] == board[24] == board[25] == ' ':
        return True
    elif board[1] == board[6] == board[11] == board[16] == board[21] == ' ':
        return True
    elif board[2] == board[7] == board[12] == board[17] == board[22] == ' ':
        return True
    elif board[3] == board[8] == board[13] == board[18] == board[23] == ' ':
        return True
    elif board[4] == board[9] == board[14] == board[19] == board[24] == ' ':
        return True
    elif board[5] == board[10] == board[15] == board[20] == board[25] == ' ':
        return True
    elif board[1] == board[7] == board[13] == board[19] == board[25] == ' ':
        return True
    elif board[5] == board[9] == board[13] == board[17] == board[21] == ' ':
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
            if letter=='x':
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

def playerMove():
    position = int(input('Choose a position for O:\t'))
    insertLetter('o', board, position)

def botMove():
    position = int(input('Choose a position for X:\t'))
    insertLetter('x', board, position)

while not checkWinner():
    botMove()
    playerMove()




