import game

def game_loop(chess):

    print("Welcome to Chess! Enter moves by typing the starting square's coordinates followed by the destination space.")
    print("Separate them with a space only, like this: b2 b3")
    print("The game follows all traditional chess rules. Enjoy!")

    while chess.get_game_state() != "CHECKMATE" and chess.get_game_state() != "STALEMATE":
        coords = input(f"{chess.get_turn()}'s turn: ").split()
        chess.make_move(coords[0],coords[1])

def main():

    while True:
        chess = game.Game()
        game_loop(chess)
        if chess.get_game_state() == "STALTEMATE":
            print("Stalemate! A new game will begin.")
        if chess.get_game_state() == "CHECKMATE":
            if chess.get_turn() == "white":
                print("Checkmate! Black wins! A new game will begin.")
            else:
                print("Checkmate! White wins! A new game will begin.")


main()



