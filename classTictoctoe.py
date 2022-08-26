
from statistics import mean

from newOne import checkDraw


class TictoctoeGame:
    def __init__(self):
        self.board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ',10: ' ',
         11: ' ',12: ' ',13: ' ',14: ' ',15: ' ',
         16: ' ',17: ' ',18: ' ',19: ' ',20: ' ',
         21: ' ',22: ' ',23: ' ',24: ' ',25: ' '}
        self.player = 'o'
        self.bot = 'x'
    def printBoard(self):
        board = f"_________\n{self.board[1]}|{self.board[2]}|{self.board[3]}|{self.board[4]}|{self.board[5]}\n-+-+-+-+-\n{self.board[6]}|{self.board[7]}|{self.board[8]}|{self.board[9]}|{self.board[10]}\n-+-+-+-+-\n{self.board[11]}|{self.board[12]}|{self.board[13]}|{self.board[14]}|{self.board[15]}\n-+-+-+-+-\n{self.board[16]}|{self.board[17]}|{self.board[18]}|{self.board[19]}|{self.board[20]}\n-+-+-+-+-\n{self.board[21]}|{self.board[22]}|{self.board[23]}|{self.board[24]}|{self.board[25]}\n"
        return board

    # def spaceIsFree(self, position):
    #     return self.board[position] == ' '
    
    def checkWinner(self):
        if self.board[1] == self.board[2] == self.board[3] == self.board[4] == self.board[5] != ' ':
            return True
        elif self.board[6] == self.board[7] == self.board[8] == self.board[9] == self.board[10] != ' ':
            return True
        elif self.board[11] == self.board[12] == self.board[13] == self.board[14] == self.board[15] != ' ':
            return True
        elif self.board[16] == self.board[17] == self.board[18] == self.board[19] == self.board[20] != ' ':
            return True
        elif self.board[21] == self.board[22] == self.board[23] == self.board[24] == self.board[25] != ' ':
            return True
        elif self.board[1] == self.board[6] == self.board[11] == self.board[16] == self.board[21] != ' ':
            return True
        elif self.board[2] == self.board[7] == self.board[12] == self.board[17] == self.board[22] != ' ':
            return True
        elif self.board[3] == self.board[8] == self.board[13] == self.board[18] == self.board[23] != ' ':
            return True
        elif self.board[4] == self.board[9] == self.board[14] == self.board[19] == self.board[24] != ' ':
            return True
        elif self.board[5] == self.board[10] == self.board[15] == self.board[20] == self.board[25] != ' ':
            return True
        elif self.board[1] == self.board[7] == self.board[13] == self.board[19] == self.board[25] != ' ':
            return True
        elif self.board[5] == self.board[9] == self.board[13] == self.board[17] == self.board[21] != ' ':
            return True
        else:
            return False
    def checkDraw(self):
        for k in self.board.values():
            if k == ' ':
                return False
        else:
            return True
    def insertLetter(self, position, letter):
        if position not in self.board.keys():
            return "invalid position, enter a number between 1 and 25"
        if self.board[position] != ' ':
            return "this position is already taken"
        else:
            self.board[position] = letter
            if self.checkDraw():
                return "Game Draw"
            if self.checkWhichMarkWon('x', self.board) or self.checkWhichMarkWon('o', self.board):
                if letter == self.player:
                    return "You Won"
                else:
                    return "Bot Won"
            
            return True
                
    
    def botMove(self):
        bestScore =-800
        bestMove = 0
        for key in self.board.keys():
            if self.board[key]==' ':
                self.board[key]=self.bot
                score=self.miniMax(self.board,8, False)
                self.board[key]=' '
                if score>bestScore:
                    bestScore=score
                    bestMove=key
        return(self.insertLetter(bestMove, self.bot))
    
    def heuristic(self,board):
        scores = []

            #botloop
        if not (board[1] == self.player or board[2] == self.player or board[3] == self.player or board[4] == self.player or board[5] == self.player):
            sum = 0
            for i in range(1,6):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[6] == self.player or board[7] == self.player or board[8] == self.player or board[9] == self.player or board[10] == self.player):
            sum = 0
            for i in range(6,11):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[11] == self.player or board[12] == self.player or board[13] == self.player or board[14] == self.player or board[15] == self.player):
            sum = 0
            for i in range(11,16):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[16] == self.player or board[17] == self.player or board[18] == self.player or board[19] == self.player or board[20] == self.player):
            sum = 0
            for i in range(16,21):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[21] == self.player or board[22] == self.player or board[23] == self.player or board[24] == self.player or board[25] == self.player):
            sum = 0
            for i in range(21,26):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[1] == self.player or board[6] == self.player or board[11] == self.player or board[16] == self.player or board[21] == self.player):
            sum = 0
            for i in range(1,21,5):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[2] == self.player or board[7] == self.player or board[12] == self.player or board[17] == self.player or board[22] == self.player):
            sum = 0
            for i in range(2,22,5):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[3] == self.player or board[8] == self.player or board[13] == self.player or board[18] == self.player or board[23] == self.player):
            sum = 0
            for i in range(3,23,5):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[4] == self.player or board[9] == self.player or board[14] == self.player or board[19] == self.player or board[24] == self.player):
            sum = 0
            for i in range(4,24,5):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[5] == self.player or board[10] == self.player or board[15] == self.player or board[20] == self.player or board[25] == self.player):
            sum = 0
            for i in range(5,26,5):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[1] == self.player or board[7] == self.player or board[13] == self.player or board[19] == self.player or board[25] == self.player):
            sum = 0
            for i in range(1,26,6):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        if not (board[5] == self.player or board[9] == self.player or board[13] == self.player or board[17] == self.player or board[21] == self.player):
            sum = 0
            for i in range(5,22,4):
                if board[i] == self.bot:
                    sum += i
            scores.append(sum/5)
        #self.playerloop
        if not (board[1] == self.bot or board[2] == self.bot or board[3] == self.bot or board[4] == self.bot or board[5] == self.bot):
            sum = 0
            for i in range(1,6):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[6] == self.bot or board[7] == self.bot or board[8] == self.bot or board[9] == self.bot or board[10] == self.bot):
            sum = 0
            for i in range(6,11):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[11] == self.bot or board[12] == self.bot or board[13] == self.bot or board[14] == self.bot or board[15] == self.bot):
            sum = 0
            for i in range(11,16):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[16] == self.bot or board[17] == self.bot or board[18] == self.bot or board[19] == self.bot or board[20] == self.bot):
            sum = 0
            for i in range(16,21):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[21] == self.bot or board[22] == self.bot or board[23] == self.bot or board[24] == self.bot or board[25] == self.bot):
            sum = 0
            for i in range(21,26):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[1] == self.bot or board[6] == self.bot or board[11] == self.bot or board[16] == self.bot or board[21] == self.bot):
            sum = 0
            for i in range(1,21,5):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[2] == self.bot or board[7] == self.bot or board[12] == self.bot or board[17] == self.bot or board[22] == self.bot):
            sum = 0
            for i in range(2,22,5):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[3] == self.bot or board[8] == self.bot or board[13] == self.bot or board[18] == self.bot or board[23] == self.bot):
            sum = 0
            for i in range(3,23,5):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[4] == self.bot or board[9] == self.bot or board[14] == self.bot or board[19] == self.bot or board[24] == self.bot):
            sum = 0
            for i in range(4,24,5):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[5] == self.bot or board[10] == self.bot or board[15] == self.bot or board[20] == self.bot or board[25] == self.bot):
            sum = 0
            for i in range(5,26,5):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[1] == self.bot or board[7] == self.bot or board[13] == self.bot or board[19] == self.bot or board[25] == self.bot):
            sum = 0
            for i in range(1,26,6):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)
        if not (board[5] == self.bot or board[9] == self.bot or board[13] == self.bot or board[17] == self.bot or board[21] == self.bot):
            sum = 0
            for i in range(5,22,4):
                if board[i] == self.player:
                    sum -= i
            scores.append(sum/5)

        score = mean(scores)

            
                    
        return score


    def checkWhichMarkWon(self,mark,board):
        
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
    def miniMax(self,board,depth,isMaximizing):
        
        
        if self.checkWhichMarkWon(self.bot,board):
            return 1
        elif self.checkWhichMarkWon(self.player,board):
            return -1
        elif self.checkDraw() or depth==5:
            return 0
        elif depth==0:
            return self.heurestic(board)
        if isMaximizing:
            bestScore=-800
                
            for key in board.keys():
                if board[key]==' ':
                    board[key]=self.bot
                    score=self.miniMax(board,depth-1, False)
                    
                    board[key]=' '
                        
                    if score>bestScore:
                        bestScore=score

            return bestScore
                            
        else:
            bestScore=800
            for key in board.keys():
                if board[key]==' ':
                    board[key]=self.player
                    score=self.miniMax(board, depth-1, True)
                    board[key]=' '
                    if score<bestScore:
                        bestScore=score
            return bestScore


game = TictoctoeGame()

# while True:
#     playerInput = int(input("Enter your move: "))
    
#     print(game.insertLetter(playerInput, game.player))
#     print(game.printBoard())
#     # game.printBoard()
#     print(game.botMove())
#     print(game.printBoard())