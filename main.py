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
    pass
def checkDraw(board):
    pass
    # if ' ' in board.values():
    #     return False
    # else:
    #     return True

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

insertLetter('o', board, 1)
insertLetter('o', board, 1)