import chess
import bot

board = chess.Board()


if __name__ == "__main__":
    chessBot = bot.randomBot("BLACK") 
    print("welcome to chess")
    
    while not board.is_game_over():
        ### USER TURN ###
        validMove = False
        while not validMove:
            print(board)
            print("viable moves: ", board.legal_moves)
            print("input your move")
            try:
                inputMove = input()
                move = board.parse_san(inputMove)
            except ValueError:
                print("that is not a valid move, try again!")
            finally:
                validMove = True
                board.push(move)
        ### BOT TURN ###
        chessBotMove = chessBot.getMove(board)
        board.push(chessBotMove)
        print("chessBot made the move ", chessBotMove)

