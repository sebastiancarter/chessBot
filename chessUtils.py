import chess
import numpy as np
def isWin(board, colour):
    if not board.is_game_over():
        return False
    else:
        outcome = board.outcome()
        # Did someone win?
        if outcome is None:
            return False
        if outcome.winner is None:
            return False
        elif outcome.winner == colour:
            return True

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}
def getMaterial(board, colour):
    occ = board.occupied_co[colour]
    # get the number of pawns on the board and the color
    counts = np.array([
        (board.pawns   & occ).bit_count(), # bit_count counts the number of 1s in the binary version of the board
        (board.knights & occ).bit_count(), # which essentially gives us the count in a super efficient way
        (board.bishops & occ).bit_count(),
        (board.rooks   & occ).bit_count(),
        (board.queens  & occ).bit_count(),
    ], dtype=np.int16)
    values = np.array([1, 3, 3, 5, 9], dtype=np.int16)
    # return the dot product of the counts and values
    return int(counts @ values)