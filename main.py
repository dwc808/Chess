import game

print("Welcome to Chess! Enter moves by typing the starting square's coordinates followed by the destination space.")
print("Separate them with a space only, like this: b2 b3")
print("The game follows all traditional chess rules. Enjoy!")

chess = game.Game()

for piece in chess._pieces.values():
    piece.set_position((10, 10))
    piece.set_status("dead")
    piece.clear_valid_moves()

for square in chess._squares.values():
    square.set_piece(None)

    # initialize pieces
chess._pieces['black_king'].set_position((0, 7))
chess._pieces['black_king'].set_status("alive")
chess._pieces['white_king'].set_position((2, 3))
chess._pieces['white_king'].set_status("alive")
chess._pieces['white_queen'].set_position((5, 6))
chess._pieces['white_queen'].set_status("alive")
chess._pieces['white_king'].has_moved = True
chess._pieces['black_king'].has_moved = True

chess._squares["f7"].set_piece(chess._pieces["white_queen"])
chess._squares["a8"].set_piece(chess._pieces["black_king"])
chess._squares["c4"].set_piece(chess._pieces["white_king"])

chess.print_board()
chess.refresh_valid_moves()

chess.make_move('f7', 'c7')

while chess.get_game_state() != "CHECKMATE" and chess.get_game_state() != "STALEMATE":
    coords = input(f"{chess.get_turn()}'s turn: ").split()
    chess.make_move(coords[0],coords[1])
    chess.print_board()


