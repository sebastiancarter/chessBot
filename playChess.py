import chess
import bot

board = chess.Board()


if __name__ == "__main__":
    validInput = False
    print("welcome to chess")
    print("you are playing as white, the bot is playing as black")
    while not validInput:
        print("what bot do you want to play against? (type the number)")
        print("1. randomBot")
        print("2. minimaxBot")
        inputBot = input()
        if inputBot == "1":
            chessBot = bot.randomBot(chess.BLACK)
            validInput = True
        elif inputBot == "2":
            chessBot = bot.minimaxBot(chess.BLACK)
            validInput = True
        else:
            print("that is not a valid input, try again!")
    
    while not board.is_game_over():
        ### USER TURN ###
        validMove = False
        while not validMove:
            print(board)
            print("viable moves: ", board.legal_moves)
            print("input your move")
            try:
                inputMove = input()
                if inputMove == "quit":
                    print("quitting game...")
                    exit()
                move = board.parse_san(inputMove)
            except ValueError:
                print("that is not a valid move, try again!")
                continue
            if board.is_legal(move):
                board.push(move)
                validMove = True
            else:
                print("that is not a legal move!")
        ### BOT TURN ###
        chessBotMove = chessBot.getMove(board)
        if chessBotMove is None:
            print("chessBot has no legal moves, you win!")
            break
        else:
            board.push(chessBotMove)
            print("chessBot made the move ", chessBotMove)
    print("thank you for playing!")
    print("the final board state was: ")
    print(board)
    print("the result was: ", board.outcome())

