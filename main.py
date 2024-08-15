import game

print("Welcome to Chess! Enter moves by typing the starting square's coordinates followed by the destination space.")
print("Separate them with a space only, like this: b2 b3")
print("The game follows all traditional chess rules. Enjoy!")

chess = game.Game()
chess.make_move("b1", "a3")
chess.make_move("h7", "h6")
chess.make_move("b2", "b3")
chess.make_move("h6", "h5")
chess.make_move("c1","b2")
chess.make_move("h5", "h4")
chess.make_move("e2", "e3")
chess.make_move("h4", "h3")
chess.make_move("d1","e2")
chess.make_move("h3", "g2")
chess.make_move("e1","c1")

while chess.get_game_state() != "CHECKMATE" and chess.get_game_state() != "STALEMATE":
    coords = input(f"{chess.get_turn()}'s turn: ").split()
    chess.make_move(coords[0],coords[1])
    chess.print_board()


