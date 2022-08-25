
from audioop import avg
from statistics import mean


bot= 'x'
player='o'

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ',10: ' ',
         11: ' ',12: ' ',13: ' ',14: ' ',15: ' ',
         16: ' ',17: ' ',18: ' ',19: ' ',20: ' ',
         21: ' ',22: ' ',23: ' ',24: ' ',25: ' '}

def printBoard(board):
    print("_________")
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
    print("*********")



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
    if position not in board.keys():
        print('Invalid position')
        printBoard(board)
        position = int(input('Choose a different position:\t'))
        insertLetter(letter, board, position)
    elif spaceIsFree(board, position):
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
    print()
    position = int(input('Choose a position for O:\t'))
    
    insertLetter(player, board, position)

def botMove():
    bestScore=-800
    bestMove=0
    for key in board.keys():
        if board[key]==' ':
            board[key]=bot
            score=miniMax(board,8, False)
            board[key]=' '
            if score>bestScore:
                bestScore=score
                bestMove=key
    insertLetter(bot, board, bestMove)
def heurestic(board):
    
    scores=[]

    #botloop
    if not (board[1] == player or board[2] == player or board[3] == player or board[4] == player or board[5] == player):
        sum = 0
        for i in range(1,6):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[6] == player or board[7] == player or board[8] == player or board[9] == player or board[10] == player):
        sum = 0
        for i in range(6,11):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[11] == player or board[12] == player or board[13] == player or board[14] == player or board[15] == player):
        sum = 0
        for i in range(11,16):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[16] == player or board[17] == player or board[18] == player or board[19] == player or board[20] == player):
        sum = 0
        for i in range(16,21):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[21] == player or board[22] == player or board[23] == player or board[24] == player or board[25] == player):
        sum = 0
        for i in range(21,26):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[1] == player or board[6] == player or board[11] == player or board[16] == player or board[21] == player):
        sum = 0
        for i in range(1,21,5):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[2] == player or board[7] == player or board[12] == player or board[17] == player or board[22] == player):
        sum = 0
        for i in range(2,22,5):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[3] == player or board[8] == player or board[13] == player or board[18] == player or board[23] == player):
        sum = 0
        for i in range(3,23,5):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[4] == player or board[9] == player or board[14] == player or board[19] == player or board[24] == player):
        sum = 0
        for i in range(4,24,5):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[5] == player or board[10] == player or board[15] == player or board[20] == player or board[25] == player):
        sum = 0
        for i in range(5,26,5):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[1] == player or board[7] == player or board[13] == player or board[19] == player or board[25] == player):
        sum = 0
        for i in range(1,26,6):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    if not (board[5] == player or board[9] == player or board[13] == player or board[17] == player or board[21] == player):
        sum = 0
        for i in range(5,22,4):
            if board[i] == bot:
                sum += i
        scores.append(sum/5)
    #playerloop
    if not (board[1] == bot or board[2] == bot or board[3] == bot or board[4] == bot or board[5] == bot):
        sum = 0
        for i in range(1,6):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[6] == bot or board[7] == bot or board[8] == bot or board[9] == bot or board[10] == bot):
        sum = 0
        for i in range(6,11):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[11] == bot or board[12] == bot or board[13] == bot or board[14] == bot or board[15] == bot):
        sum = 0
        for i in range(11,16):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[16] == bot or board[17] == bot or board[18] == bot or board[19] == bot or board[20] == bot):
        sum = 0
        for i in range(16,21):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[21] == bot or board[22] == bot or board[23] == bot or board[24] == bot or board[25] == bot):
        sum = 0
        for i in range(21,26):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[1] == bot or board[6] == bot or board[11] == bot or board[16] == bot or board[21] == bot):
        sum = 0
        for i in range(1,21,5):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[2] == bot or board[7] == bot or board[12] == bot or board[17] == bot or board[22] == bot):
        sum = 0
        for i in range(2,22,5):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[3] == bot or board[8] == bot or board[13] == bot or board[18] == bot or board[23] == bot):
        sum = 0
        for i in range(3,23,5):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[4] == bot or board[9] == bot or board[14] == bot or board[19] == bot or board[24] == bot):
        sum = 0
        for i in range(4,24,5):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[5] == bot or board[10] == bot or board[15] == bot or board[20] == bot or board[25] == bot):
        sum = 0
        for i in range(5,26,5):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[1] == bot or board[7] == bot or board[13] == bot or board[19] == bot or board[25] == bot):
        sum = 0
        for i in range(1,26,6):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)
    if not (board[5] == bot or board[9] == bot or board[13] == bot or board[17] == bot or board[21] == bot):
        sum = 0
        for i in range(5,22,4):
            if board[i] == player:
                sum -= i
        scores.append(sum/5)

    score = mean(scores)

        
                
    return score

    

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
    elif depth==0:
        return heurestic(board)
    if isMaximizing:
        bestScore=-800
        
        for key in board.keys():
            if board[key]==' ':
                board[key]=bot
                score=miniMax(board,depth-1, False)
                board[key]=' '
                
                if score>bestScore:
                    bestScore=score

        return bestScore
                    
    else:
        bestScore=800
        for key in board.keys():
            if board[key]==' ':
                board[key]=player
                score=miniMax(board, depth-1, True)
                board[key]=' '
                if score<bestScore:
                    bestScore=score
        return bestScore

def game():
        while not checkWinner(board):
            playerMove(board)
            botMove()
if __name__ == '__main__':
        
    while not checkWinner(board):
        playerMove(board)
        botMove()
        




