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
        self.assertEqual(chess.make_move('f5', 'e5'), True)

    def test_castle(self):
        pass

    def test_revive(self):
        pass

if __name__ == '__main__':
    unittest.main()

