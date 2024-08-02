import game

print("Welcome to Chess! Enter moves by typing the starting square's coordinates followed by the destination space.")
print("Separate them with a space only, like this: b2 b3")
print("The game follows all traditional chess rules. Enjoy!")

chess = game.Game()

chess.initialize_squares()
chess.initialize_pieces()
chess.refresh_valid_moves()

chess.make_move('e2', 'e3')
chess.make_move('d7', 'd6')
chess.make_move('b1', 'c3')
chess.make_move('c8', 'g4')
        # king can't move self into check
chess.make_move('e1', 'e2')

chess.make_move('f2', 'f4')
chess.make_move('e7', 'e6')
chess.make_move('g1', 'f3')
chess.make_move('d8', 'h4')
        #can't make any moves that don't address check
chess.make_move('c2', 'a4')
chess.make_move('e1', 'f2')

        #piece can move if they enter path of checking piece
chess.make_move('g2', 'g3')
chess.make_move('h4', 'g3')

        #piece can move if they capture checking piece
chess.make_move('h2', 'g3')

        #king can move itself out of check TODO

while chess.get_game_state() != "CHECKMATE" and chess.get_game_state() != "STALEMATE":
    coords = input(f"{chess.get_turn()}'s turn: ").split()
    chess.make_move(coords[0],coords[1])
    chess.print_board()


