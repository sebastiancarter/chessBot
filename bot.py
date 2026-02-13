import chess
import random
import chessUtils
import datetime

class chessBot:
    def __init__(self, colour):
        self.colour = colour

    def getMove(self, board):
        pass


class randomBot(chessBot):
    def __init__(self, colour):
        super().__init__(colour)

    def getMove(self, board):
        moves = list(board.legal_moves)
        return random.choice(moves)

class minimaxBot(chessBot):
    def __init__(self, colour):
        super().__init__(colour)
        self.depth = 3
        self.colour = colour


    def maxVal(self, board, currDepth):
        if currDepth == 0 or board.is_game_over():
            return self.evaluationFunc(board), None
        
        maxValue = None
        bestAction = None
        actions = list(board.legal_moves)
        for action in actions:
            board.push(action)
            (score, nextBestAction) = self.minVal(board, currDepth - 1)
            board.pop()
            if maxValue == None or score > maxValue:
                maxValue = score
                bestAction = action
        return (maxValue, bestAction)
    
    def minVal(self, board, currDepth):
        if currDepth == 0 or board.is_game_over():
            return self.evaluationFunc(board), None
        
        minValue = None
        bestAction = None
        actions = list(board.legal_moves)
        for action in actions:
            board.push(action)
            (score, nextBestAction) = self.maxVal(board, currDepth - 1)
            board.pop()
            if minValue == None or score < minValue:
                minValue = score
                bestAction = action
        return (minValue, bestAction)

    def getMove(self, board):
        (score, bestAction) = self.maxVal(board, self.depth)
        return bestAction  


    def evaluationFunc(self, board):
        # print every ten seconds to show we still care
        if chessUtils.isWin(board, self.colour):
            return 1000
        elif chessUtils.isWin(board, not self.colour): # TODO: will need to handle this when I implement choosing colour
            return -1000
        elif board.is_stalemate():
            return 0
        else:
            botMaterial = chessUtils.getMaterial(board, self.colour)
            playerMaterial = chessUtils.getMaterial(board, not self.colour)
            return botMaterial - playerMaterial
