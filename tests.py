import unittest
import game

class BasicPlay(unittest.TestCase):

    def test_normal_play(self):
        """Test a basic set of moves, taking normal turns."""
        chess = game.Game()
        chess.initialize_squares()
        chess.initialize_pieces()
        chess.refresh_valid_moves()

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

    def test_check(self):
        pass

    def test_checkmate(self):
        pass

    def test_stalemate(self):
        pass

class SpecialMoves(unittest.TestCase):

    def test_enpassant(self):
        chess = game.Game()
        chess.initialize_squares()
        chess.initialize_pieces()
        chess.refresh_valid_moves()
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

#Class Invalid_moves(unittest.TestCase):

 #   def test_invalid_pawn_captures:
  #      pass

   # def test_invalid_bqc_captures:
    #    pass


if __name__ == '__main__':
    unittest.main()

