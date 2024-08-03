import unittest
import game

class BasicPlay(unittest.TestCase):

    def test_normal_play(self):
        """Test a basic set of moves, taking normal turns."""
        chess = game.Game()

        self.assertEqual(chess.make_move('b2','b3'), True)
        self.assertEqual(chess.make_move('e7','e5'), True)
        self.assertEqual(chess.make_move('g1', 'h3'), True)
        self.assertEqual(chess.make_move('d7', 'd5'), True)
        self.assertEqual(chess.make_move('c1', 'a3'), True)
        self.assertEqual(chess.make_move('c7', 'c5'), True)
        self.assertEqual(chess.make_move('f2', 'f4'), True)
        self.assertEqual(chess.make_move('b8', 'd7'), True)
        self.assertEqual(chess.make_move('f4', 'e5'), True)
        self.assertEqual(chess.make_move('d5', 'd4'), True)
        self.assertEqual(chess.make_move('c2', 'c3'), True)
        self.assertEqual(chess.make_move('h7', 'h5'), True)
        self.assertEqual(chess.make_move('c3', 'd4'), True)
        self.assertEqual(chess.make_move('b7', 'b6'), True)
        self.assertEqual(chess.make_move('b1', 'c3'), True)
        self.assertEqual(chess.make_move('c8', 'a6'), True)

    def test_check_and_check_mate(self):
        chess = game.Game()

        self.assertEqual(chess.make_move('e2', 'e3'), True)
        self.assertEqual(chess.make_move('d7', 'd6'), True)
        self.assertEqual(chess.make_move('b1', 'c3'), True)
        self.assertEqual(chess.make_move('c8', 'g4'), True)
        # king can't move self into check
        self.assertEqual(chess.make_move('e1', 'e2'), False)

        self.assertEqual(chess.make_move('f2', 'f4'), True)
        self.assertEqual(chess.make_move('e7', 'e6'), True)
        self.assertEqual(chess.make_move('g1', 'f3'), True)
        self.assertEqual(chess.make_move('d8', 'h4'), True)
        #can't make any moves that don't address check
        self.assertEqual(chess.make_move('c3', 'a4'), False)
        self.assertEqual(chess.make_move('e1', 'f2'), False)

        #piece can move if they enter path of checking piece
        self.assertEqual(chess.make_move('g2', 'g3'), True)
        self.assertEqual(chess.make_move('h4', 'g3'), True)

        #piece can move if they capture checking piece
        self.assertEqual(chess.make_move('h2', 'g3'), True)

        #king can move itself out of check TODO

    def test_checkmate(self):
        """Test that checkmate occurs when a player is in check and has no valid moves."""
        chess = game.Game()

        self.assertEqual(chess.make_move('e2', 'e4'), True)
        self.assertEqual(chess.make_move('f7', 'f5'), True)
        self.assertEqual(chess.make_move('e4', 'f5'), True)
        self.assertEqual(chess.make_move('g7', 'g5'), True)
        self.assertEqual(chess.make_move('d1', 'h5'), True)
        self.assertEqual(chess.get_game_state(), "CHECKMATE")

    def test_stalemate(self):
        """Test that stalemate occurs when a player has no valid moves but is not in check."""
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

        chess._squares["f7"].set_piece(chess._pieces["white_queen"])
        chess._squares["a8"].set_piece(chess._pieces["black_king"])
        chess._squares["c4"].set_piece(chess._pieces["white_king"])

        chess.print_board()
        chess.refresh_valid_moves()

        chess.make_move('f7', 'c7')

        self.assertEqual(chess.get_game_state(), "STALEMATE")




class SpecialMoves(unittest.TestCase):

    def test_enpassant(self):
        chess = game.Game()

        self.assertEqual(chess.make_move('f2', 'f4'), True)
        self.assertEqual(chess.make_move('c7', 'c6'), True)
        self.assertEqual(chess.make_move('f4', 'f5'), True)
        self.assertEqual(chess.make_move('e7', 'e5'), True)
        self.assertEqual(chess.make_move('f5', 'e5'), False)
        #white en passant
        self.assertEqual(chess.make_move('f5', 'e6'), True)
        self.assertEqual(chess.make_move('c6', 'c5'), True)
        self.assertEqual(chess.make_move('h2', 'h3'), True)
        self.assertEqual(chess.make_move('c5', 'c4'), True)
        self.assertEqual(chess.make_move('d2', 'd4'), True)
        #black en passant
        self.assertEqual(chess.make_move('c4', 'd4'), False)
        self.assertEqual(chess.make_move('c4', 'd3'), True)
        self.assertEqual(chess.make_move('a2', 'a4'), True)
        self.assertEqual(chess.make_move('b7', 'b5'), True)
        self.assertEqual(chess.make_move('h3', 'h4'), True)
        self.assertEqual(chess.make_move('b5', 'b4'), True)
        self.assertEqual(chess.make_move('h4', 'h5'), True)
        # no en passant - piece didn't move last turn
        self.assertEqual(chess.make_move('b4', 'a3'), False)

    def test_castle(self):
        pass

    def test_revive(self):
        pass

class InvalidMoves(unittest.TestCase):
    """Test moves that should be disallowed."""

    def test_invalid_pawn_captures(self):

        chess = game.Game()

        self.assertEqual(chess.make_move('b2', 'b3'), True)
        self.assertEqual(chess.make_move('e7', 'e5'), True)
        self.assertEqual(chess.make_move('g1', 'h3'), True)
        self.assertEqual(chess.make_move('d7', 'd5'), True)
        self.assertEqual(chess.make_move('b1', 'c3'), True)
        self.assertEqual(chess.make_move('c7', 'c6'), True)
        self.assertEqual(chess.make_move('c3', 'e4'), True)
        self.assertEqual(chess.make_move('e5', 'e4'), False)

    def test_invalid_bqc_captures(self):
        pass


if __name__ == '__main__':
    unittest.main()

