import game

print("Welcome to Chess! Enter moves by typing the starting square's coordinates followed by the destination space.")
print("Separate them with a space only, like this: b2 b3")
print("The game follows all traditional chess rules. Enjoy!")

chess = game.Game()

while chess.get_game_state() != "CHECKMATE" and chess.get_game_state() != "STALEMATE":
    coords = input(f"{chess.get_turn()}'s turn: ").split()
    chess.make_move(coords[0],coords[1])

