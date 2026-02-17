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
        self.depth = 5
        self.colour = colour


    def maxVal(self, board, alpha, beta, currDepth):
        if currDepth == 0 or board.is_game_over():
            return self.evaluationFunc(board, currDepth), None
        
        maxValue = None
        bestAction = None
        actions = list(board.legal_moves)
        for action in actions:
            board.push(action)
            (score, nextBestAction) = self.minVal(board, alpha, beta, currDepth - 1)
            board.pop()
            if maxValue == None or score > maxValue:
                maxValue = score
                bestAction = action
            # TODO: figure out if this should be here
            if beta is not None and maxValue > beta:
                return (maxValue, bestAction)
            
            if alpha is None:
                alpha = maxValue
            else:
                alpha = max(alpha, maxValue)
        return (maxValue, bestAction)
    
    def minVal(self, board, alpha, beta, currDepth):
        if currDepth == 0 or board.is_game_over():
            return self.evaluationFunc(board, currDepth), None
        
        minValue = None
        bestAction = None
        actions = list(board.legal_moves)
        for action in actions:
            board.push(action)
            (score, nextBestAction) = self.maxVal(board, alpha, beta, currDepth - 1)
            board.pop()
            if minValue == None or score < minValue:
                minValue = score
                bestAction = action
            if alpha is not None and minValue < alpha:
                return (minValue, bestAction)
            if beta is None:
                beta = minValue
            else:
                beta = min(beta, minValue)
        return (minValue, bestAction)

    def getMove(self, board):
        (score, bestAction) = self.maxVal(board, None, None, self.depth)
        return bestAction  

    def moveOrderingFunc(self, moveList):
        # TODO: implement a move ordering function to improve speed
        pass

    def evaluationFunc(self, board, depth):
        # TODO: add some positional evaluation stuff
        if chessUtils.isWin(board, self.colour):
            return 1000-depth
        elif chessUtils.isWin(board, not self.colour): 
            return -1000
        elif board.is_stalemate() and self.colour == chess.BLACK:
            return 500
        elif board.is_stalemate() and self.colour == chess.WHITE:
            return -500
        else:
            botMaterial = chessUtils.getMaterial(board, self.colour)
            playerMaterial = chessUtils.getMaterial(board, not self.colour)
            return botMaterial - playerMaterial
