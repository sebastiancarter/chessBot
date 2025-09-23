import chess
import random



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

