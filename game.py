from square import Square
from piece import Piece, King, Pawn, Knight, Castle, Queen, Bishop
class Game:
    """This class runs the core of the chess game."""

    def __init__(self):
        self._squares = {}
        self._pieces = {}
        self._all_valid_moves = []
        self._turn = "white"
        self._game_state = "UNFINISHED"
        self.initialize_squares()
        self.initialize_pieces()
        self._vulnerable = None
        self.print_board()
        self.refresh_valid_moves()


    def initialize_squares(self):
        """This method creates the Squares for the board. Each Square is initialized
        with x and y coordinates, a name that matches the coordinates a player will use
        (such as a3), and a color, which alternates to match the typical pattern of
        a chess board.
        """

        x = -1  # x-coordinate
        y = 0  # y-coordinate

        for letter in "abcdefgh":
            y = 0
            x += 1
            if x % 2 == 0:
                color = "black"
            else:
                color = "white"

            for number in range(1, 9):
                self._squares[letter + str(number)] = Square(letter + str(number), (x, y), color)
                y += 1
                if color == "black":
                    color = "white"
                else:
                    color = "black"

    def initialize_pieces(self):
        """This method initializes the Pieces. Each Piece object is given a name
        to match the specific chess piece it represents, a color, starting coordinates,
        and a starting status of 'alive.'
        """

        self._pieces['black_king'] = King("black", "king", (4, 7), "alive")
        self._squares["e8"].set_piece(self._pieces['black_king'])
        self._pieces['white_king'] = King("white", "king", (4, 0), "alive")
        self._squares["e1"].set_piece(self._pieces['white_king'])

        self._pieces['black_castle'] = Castle("black", "castle", (0, 7), "alive")
        self._squares["a8"].set_piece(self._pieces['black_castle'])
        self._pieces['white_castle'] = Castle("white", "castle", (0, 0), "alive")
        self._squares["a1"].set_piece(self._pieces['white_castle'])
        self._pieces['black_castle_2'] = Castle("black", "castle", (7, 7), "alive")
        self._squares["h8"].set_piece(self._pieces['black_castle_2'])
        self._pieces['white_castle_2'] = Castle("white", "castle", (7, 0), "alive")
        self._squares["h1"].set_piece(self._pieces['white_castle_2'])

        self._pieces['black_bishop'] = Bishop("black", "bishop", (2, 7), "alive")
        self._squares["c8"].set_piece(self._pieces['black_bishop'])
        self._pieces['black_bishop_2'] = Bishop("black", "bishop", (5, 7), "alive")
        self._squares["f8"].set_piece(self._pieces['black_bishop_2'])
        self._pieces['white_bishop'] = Bishop("white", "bishop", (2, 0), "alive")
        self._squares["c1"].set_piece(self._pieces['white_bishop'])
        self._pieces['white_bishop_2'] = Bishop("white", "bishop", (5, 0), "alive")
        self._squares["f1"].set_piece(self._pieces['white_bishop_2'])

        self._pieces['black_knight'] = Knight("black", "knight", (1, 7), "alive")
        self._squares["b8"].set_piece(self._pieces['black_knight'])
        self._pieces['black_knight_2'] = Knight("black", "knight", (6, 7), "alive")
        self._squares["g8"].set_piece(self._pieces['black_knight_2'])
        self._pieces['white_knight'] = Knight("white", "knight", (1, 0), "alive")
        self._squares["b1"].set_piece(self._pieces['white_knight'])
        self._pieces['white_knight_2'] = Knight("white", "knight", (6, 0), "alive")
        self._squares["g1"].set_piece(self._pieces['white_knight_2'])

        self._pieces['black_queen'] = Queen("black", "queen", (3, 7), "alive")
        self._squares["d8"].set_piece(self._pieces['black_queen'])
        self._pieces['white_queen'] = Queen("white", "queen", (3, 0), "alive")
        self._squares["d1"].set_piece(self._pieces['white_queen'])

        #black pawns
        starter = 0
        y_name = 1
        for letter in "abcdefgh":
            self._pieces['black_pawn' + str(y_name)] = Pawn("black", "pawn", (starter, 6), "alive")
            self._squares[letter + "7"].set_piece(self._pieces['black_pawn'+str(y_name)])
            starter += 1
            y_name += 1

        # white pawns
        starter = 0
        y_name = 1
        for letter in "abcdefgh":
            self._pieces['white_pawn' + str(y_name)] = Pawn("white", "pawn", (starter, 1), "alive")
            self._squares[letter + "2"].set_piece(self._pieces['white_pawn' + str(y_name)])
            starter += 1
            y_name += 1

    def print_board(self):
        """This method prints the current state of the board. It takes no parameters. It cycles through
        all the squares in reverse order. If the square is empty, it will print that square, matching
        the color. If there is a piece present, it will print the icon for that piece. It also prints
        a key for the coordinates the player will use to move pieces.
        """

        row = 8

        for number in reversed(range(1, 9)):
            print(row, end="")

            for letter in "abcdefgh":

                # Print a square if there are no pieces on it.
                if self._squares[letter + str(number)].is_empty() == True:

                    # Print a new line when a row is finished
                    if letter == "h":
                        if self._squares[letter + str(number)].get_color() == "black":
                            print("[-]")
                            row -= 1
                        else:
                            print("[ ]")
                            row -= 1
                    else:
                        if self._squares[letter + str(number)].get_color() == "black":
                            print("[-]", end="")
                        else:
                            print("[ ]", end="")

                else:

                    if letter == "h":
                        print("[" + self._squares[letter + str(number)].get_piece().get_icon() + "]")
                        row -= 1
                    else:
                        print("[" + self._squares[letter + str(number)].get_piece().get_icon() + "]", end="")

        print("  a  b  c  d  e  f  g  h")



    def get_game_state(self):
        """Returns the current game_state."""
        return self._game_state

    def get_turn(self):
        """Returns the color of player's turn."""
        return self._turn

    def get_square(self, coords):
        """This method takes a tuple of x,y coordinates and returns the Square object at
        those coordinates.
        """

        for square in self._squares.values():
            if square.get_coords() == coords:
                return square

    def check_square(self, test_coords, piece):
        """This method takes a set of x,y coordinates (as a tuple) and a piece object as parameters.
        It then checks to see if the square at test_coords is a valid move for piece. It will update
        the valid moves for the piece if it is. It returns a string 'break' if a loop should be ended.
        This is for the castle/bishop pieces and indicates their path is blocked by another piece.
        """

        if self.get_square((test_coords[0], test_coords[1])).is_empty() == True:
            piece.add_valid_move(self.get_square((test_coords[0], test_coords[1])).get_coords())
            return
        else:
            # end if piece on own team is in way
            if self.get_square((test_coords[0], test_coords[1])).get_piece().get_color() == piece.get_color():
                return "break"
            # end but add coords if piece belongs to other player
            else:
                piece.add_valid_move((test_coords[0], test_coords[1]))
                return "break"

    def get_castle_moves(self, castle):
        """This method takes a castle object as a parameter. It will refresh the valid moves
        for that piece, given the current state of the board. It makes use of the check_square
        method to update the valid moves for the piece.
        """

        # clear previous valid moves
        castle.clear_valid_moves()

        # check up
        test_coords = list(castle.get_position())  # test coordinates are list so they can be incremented

        while test_coords[1] < 7:
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, castle)
            if check_stop == "break":
                break

        # check down
        test_coords = list(castle.get_position())

        while test_coords[1] > 0:
            test_coords[1] -= 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, castle)
            if check_stop == "break":
                break

        # check right
        test_coords = list(castle.get_position())

        while test_coords[0] < 7:
            test_coords[0] += 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, castle)
            if check_stop == "break":
                break

        # check left
        test_coords = list(castle.get_position())

        while test_coords[0] > 0:
            test_coords[0] -= 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, castle)
            if check_stop == "break":
                break

    def get_bishop_moves(self, bishop):
        """This method takes a bishop object as a parameter. It will refresh the valid moves
        for that piece, given the current state of the board. It makes use of the check_square
        method to update the valid moves for the piece.
        """

        # clear previous valid moves
        bishop.clear_valid_moves()

        # check northeast
        test_coords = list(bishop.get_position())

        while test_coords[0] < 7 and test_coords[1] < 7:
            test_coords[0] += 1
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, bishop)
            if check_stop == "break":
                break

        # check northwest
        test_coords = list(bishop.get_position())

        while test_coords[0] > 0 and test_coords[1] < 7:
            test_coords[0] -= 1
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, bishop)
            if check_stop == "break":
                break

        # check southeast
        test_coords = list(bishop.get_position())

        while test_coords[0] < 7 and test_coords[1] > 0:
            test_coords[0] += 1
            test_coords[1] -= 1
            check_stop = self.check_square(test_coords, bishop)
            if check_stop == "break":
                break

        # check southwest
        test_coords = list(bishop.get_position())

        while test_coords[0] > 0 and test_coords[1] > 0:
            test_coords[0] -= 1
            test_coords[1] -= 1
            check_stop = self.check_square(test_coords, bishop)
            if check_stop == "break":
                break

    def get_king_moves(self, king):
        """This method takes a castle object as a parameter. It will refresh the valid moves
        for that piece, given the current state of the board. It makes use of the check_square
        method to update the valid moves for the piece.
        """

        # clear previous valid moves
        king.clear_valid_moves()

        # check north
        test_coords = list(king.get_position())
        if test_coords[1] < 7:
            test_coords[1] += 1
            self.check_square(test_coords, king)

        # check northeast
        test_coords = list(king.get_position())
        if test_coords[0] < 7 and test_coords[1] < 7:
            test_coords[1] += 1
            test_coords[0] += 1
            self.check_square(test_coords, king)

        # check east
        test_coords = list(king.get_position())
        if test_coords[0] < 7:
            test_coords[0] += 1
            self.check_square(test_coords, king)

        # check southeast
        test_coords = list(king.get_position())
        if test_coords[0] < 7 and test_coords[1] > 0:
            test_coords[1] -= 1
            test_coords[0] += 1
            self.check_square(test_coords, king)

        # check south
        test_coords = list(king.get_position())
        if test_coords[1] > 0:
            test_coords[1] -= 1
            self.check_square(test_coords, king)

        # check southwest
        test_coords = list(king.get_position())
        if test_coords[0] > 0 and test_coords[1] > 0:
            test_coords[1] -= 1
            test_coords[0] -= 1
            self.check_square(test_coords, king)

        # check west
        test_coords = list(king.get_position())
        if test_coords[0] > 0:
            test_coords[0] -= 1
            self.check_square(test_coords, king)

        # check northwest
        test_coords = list(king.get_position())
        if test_coords[0] > 0 and test_coords[1] < 7:
            test_coords[1] += 1
            test_coords[0] -= 1
            self.check_square(test_coords, king)

    def get_knight_moves(self, knight):
        """This method takes a knight object as a parameter. It will refresh the valid moves
        for that piece, given the current state of the board. It makes use of the check_square
        method to update the valid moves for the piece.
        """

        # clear previous valid moves
        knight.clear_valid_moves()

        # right one, up two
        test_coords = list(knight.get_position())
        test_coords[0] += 1
        test_coords[1] += 2

        if test_coords[0] <= 7 and test_coords[1] <= 7:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # right two, up one
        test_coords = list(knight.get_position())
        test_coords[0] += 2
        test_coords[1] += 1

        if test_coords[0] <= 7 and test_coords[1] <= 7:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # right two, down one
        test_coords = list(knight.get_position())
        test_coords[0] += 2
        test_coords[1] -= 1

        if test_coords[0] <= 7 and test_coords[1] >= 0:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # right one, down two
        test_coords = list(knight.get_position())
        test_coords[0] += 1
        test_coords[1] -= 2

        if test_coords[0] <= 7 and test_coords[1] >= 0:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # left one, down two
        test_coords = list(knight.get_position())
        test_coords[0] -= 1
        test_coords[1] -= 2

        if test_coords[0] >= 0 and test_coords[1] >= 0:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # left two, down one
        test_coords = list(knight.get_position())
        test_coords[0] -= 2
        test_coords[1] -= 1

        if test_coords[0] >= 0 and test_coords[1] >= 0:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # left two, up one
        test_coords = list(knight.get_position())
        test_coords[0] -= 2
        test_coords[1] += 1

        if test_coords[0] >= 0 and test_coords[1] <= 7:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

        # left one, up two
        test_coords = list(knight.get_position())
        test_coords[0] -= 1
        test_coords[1] += 2

        if test_coords[0] >= 0 and test_coords[1] <= 7:  # test to see if move stays in bounds of board
            self.check_square(test_coords, knight)

    def get_queen_moves(self, queen):
        """Get the valid moves for a queen piece."""

        # clear previous valid moves
        queen.clear_valid_moves()

        # horizontal/vertical moves
        # check up
        test_coords = list(queen.get_position())  # test coordinates are list so they can be incremented

        while test_coords[1] < 7:
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check down
        test_coords = list(queen.get_position())

        while test_coords[1] > 0:
            test_coords[1] -= 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check right
        test_coords = list(queen.get_position())

        while test_coords[0] < 7:
            test_coords[0] += 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check left
        test_coords = list(queen.get_position())

        while test_coords[0] > 0:
            test_coords[0] -= 1
            # if the square at test_coords is empty, add that square's coordinates to piece's valid moves
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        #diagonal movement
        # check northeast
        test_coords = list(queen.get_position())

        while test_coords[0] < 7 and test_coords[1] < 7:
            test_coords[0] += 1
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check northwest
        test_coords = list(queen.get_position())

        while test_coords[0] > 0 and test_coords[1] < 7:
            test_coords[0] -= 1
            test_coords[1] += 1
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check southeast
        test_coords = list(queen.get_position())

        while test_coords[0] < 7 and test_coords[1] > 0:
            test_coords[0] += 1
            test_coords[1] -= 1
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

        # check southwest
        test_coords = list(queen.get_position())

        while test_coords[0] > 0 and test_coords[1] > 0:
            test_coords[0] -= 1
            test_coords[1] -= 1
            check_stop = self.check_square(test_coords, queen)
            if check_stop == "break":
                break

    def get_pawn_moves(self, pawn):
        """Refreshes the valid moves for a pawn."""

        #clear previous valid moves
        pawn.clear_valid_moves()

        #check for en passant
        test_coords = list(pawn.get_position())

        if self.get_square((test_coords[0]-1, test_coords[1])) != None and self.get_square((test_coords[0]-1, test_coords[1])).get_piece() == self._vulnerable:
            self.check_square((test_coords[0]-1, test_coords[1]), pawn)

        if self.get_square((test_coords[0]+1, test_coords[1])) != None and self.get_square((test_coords[0]+1, test_coords[1])).get_piece() == self._vulnerable:
            self.check_square((test_coords[0]+1, test_coords[1]), pawn)

        test_coords = list(pawn.get_position())
        #check for simple vertical movement for black pawn
        if pawn.get_color() == "black":
            test_coords[1] -= 1
            self.check_square(test_coords, pawn)
            if test_coords[1] >= 0:
                if pawn.has_moved == "no" and self.check_square(test_coords, pawn) != "break":
                    test_coords[1] -=1
                    self.check_square(test_coords, pawn)

        # check for simple vertical movement for white pawn
        else:
            test_coords[1] += 1
            self.check_square(test_coords, pawn)
            if test_coords[1] <= 7:
                if pawn.has_moved == "no" and self.check_square(test_coords, pawn) != "break":
                    test_coords[1] += 1
                    self.check_square(test_coords, pawn)

        # check for potential captures for black pawn
        if pawn.get_color() == "black":
            test_coords = list(pawn.get_position())
            test_coords[0] -= 1
            test_coords[1] -= 1
            diag_square_1 = self.get_square((test_coords[0],test_coords[1]))
            if diag_square_1 is not None:
                if diag_square_1.get_piece() is not None:
                    if diag_square_1.get_piece().get_color() == "white":
                        self.check_square(test_coords, pawn)

                test_coords = list(pawn.get_position())
                test_coords[0] += 1
                test_coords[1] -= 1
                diag_square_2 = self.get_square((test_coords[0], test_coords[1]))
                if diag_square_2 is not None:
                    if diag_square_2.get_piece() is not None:
                        if diag_square_2.get_piece().get_color() == "white":
                            self.check_square(test_coords, pawn)

        # check for potential captures for white pawn
        else:
            test_coords = list(pawn.get_position())
            test_coords[0] -= 1
            test_coords[1] += 1
            diag_square_1 = self.get_square((test_coords[0], test_coords[1]))
            if diag_square_1 is not None:
                if diag_square_1.get_piece() is not None:
                    if diag_square_1.get_piece().get_color() == "black":
                        self.check_square(test_coords, pawn)

                test_coords = list(pawn.get_position())
                test_coords[0] += 1
                test_coords[1] += 1
                diag_square_2 = self.get_square((test_coords[0], test_coords[1]))
                if diag_square_2 is not None:
                    if diag_square_2.get_piece() is not None:
                        if diag_square_2.get_piece().get_color() == "black":
                            self.check_square(test_coords, pawn)


    def refresh_valid_moves(self):
        """Refreshes the valid moves for all pieces in the game. It calls a get_[piece_type]_moves
        method for each piece on the board, which in turn call the check_square method.
        """

        if self._pieces["white_castle"].get_status() == "alive":
            self.get_castle_moves(self._pieces["white_castle"])

        if self._pieces["black_castle"].get_status() == "alive":
            self.get_castle_moves(self._pieces["black_castle"])

        if self._pieces["white_castle_2"].get_status() == "alive":
            self.get_castle_moves(self._pieces["white_castle_2"])

        if self._pieces["black_castle_2"].get_status() == "alive":
            self.get_castle_moves(self._pieces["black_castle_2"])

        if self._pieces["white_bishop"].get_status() == "alive":
            self.get_bishop_moves(self._pieces["white_bishop"])

        if self._pieces["white_bishop_2"].get_status() == "alive":
            self.get_bishop_moves(self._pieces["white_bishop_2"])

        if self._pieces["black_bishop"].get_status() == "alive":
            self.get_bishop_moves(self._pieces["black_bishop"])

        if self._pieces["black_bishop_2"].get_status() == "alive":
            self.get_bishop_moves(self._pieces["black_bishop_2"])

        if self._pieces["white_king"].get_status() == "alive":
            self.get_king_moves(self._pieces["white_king"])

        if self._pieces["black_king"].get_status() == "alive":
            self.get_king_moves(self._pieces["black_king"])

        if self._pieces["white_knight"].get_status() == "alive":
            self.get_knight_moves(self._pieces["white_knight"])

        if self._pieces["white_knight_2"].get_status() == "alive":
            self.get_knight_moves(self._pieces["white_knight_2"])

        if self._pieces["black_knight"].get_status() == "alive":
            self.get_knight_moves(self._pieces["black_knight"])

        if self._pieces["black_knight_2"].get_status() == "alive":
            self.get_knight_moves(self._pieces["black_knight_2"])

        if self._pieces["white_queen"].get_status() == "alive":
            self.get_queen_moves(self._pieces["white_queen"])

        if self._pieces["black_queen"].get_status() == "alive":
            self.get_queen_moves(self._pieces["black_queen"])

        for number in range(1,9):
            if self._pieces["black_pawn" + str(number)].get_status() == "alive":
                self.get_pawn_moves(self._pieces["black_pawn" + str(number)])

        for number in range(1,9):
            if self._pieces["white_pawn" + str(number)].get_status() == "alive":
                self.get_pawn_moves(self._pieces["white_pawn" + str(number)])

        self._all_valid_moves.clear()

        #only update white king moves if king in check
        if self._pieces["white_king"]._check == True:
            for piece in self._pieces.values():
                if piece.get_color() == "black":
                    self._all_valid_moves.append(piece.get_valid_moves())
            self._all_valid_moves.append(self._pieces["white_king"].get_valid_moves())
            return

        #only update black king moves if black king in check
        if self._pieces["black_king"]._check == True:
            for piece in self._pieces.values():
                if piece.get_color() == "white":
                    self._all_valid_moves.append(piece.get_valid_moves())
            self._all_valid_moves.append(self._pieces["black_king"].get_valid_moves())
            return

        for piece in self._pieces.values():
            self._all_valid_moves.append(piece.get_valid_moves())

    def back_up_move(self, square_1, square_2, piece_1, piece_2):
        """This method is called to reverse a move if it has caused a king to be in check."""

        # put piece 1 back on starting space
        piece_1.set_position(self._squares[square_1].get_coords())
        self._squares[square_1].set_piece(piece_1)

        # if there was a piece on square 2, set back on square 2 and set status back to alive
        if piece_2 is not None:
            piece_2.set_status("alive")
            piece_2.set_position(self._squares[square_2].get_coords())
            self._squares[square_2].set_piece(piece_2)
        else:
            self._squares[square_2].set_piece(None)

    def check_checker(self):
        """This method is called to see if a move has put either king in check. It will return
        True if a king is in check, and False otherwise."""

        white_king_position = self._pieces["white_king"].get_position()
        black_king_position = self._pieces["black_king"].get_position()

        for list in self._all_valid_moves:
            if white_king_position in list:
                self._pieces["white_king"]._check = True
                return
            elif black_king_position in list:
                self._pieces["black_king"]._check = True
                return
            else:
                self._pieces["white_king"]._check = False
                self._pieces["black_king"]._check = False

        return False

    def check_game_state(self):
        """Called after every move to check if the game state has changed. It will update the game state
        based on the current conditions."""

        if self._pieces["white_king"].get_position()[1] == 7:
            if self._game_state == "FINAL_TURN":
                if self._pieces["black_king"].get_position()[1] == 7:
                    self._game_state = "TIE"
                else:
                    self._game_state = "WHITE_WON"
            else:
                self._game_state = "FINAL_TURN"
        elif self._pieces["black_king"].get_position()[1] == 7:
            self._game_state = "BLACK_WON"

    def make_move(self, square_1, square_2):
        """This method is the command to move a piece. It takes two parameters, both strings,
        with the coordinates of the square to move from, and the square to move to. For example,
        'a1, a2'. This method checks several conditions to determine if a move can be made. It
        will first assess if the game is over, then it will ensure there is a piece on square 1.
        If there is it will make sure it's that player's turn, and check to see if square 2 is
        a valid move for that piece. If it is, it will execute the move, updating the information in
        the Square and Piece objects involved, including removing a captured piece from play. Before
        finalizing the move, it will check to make sure that neither king is in check as a result
        of the move. If either is, it will reverse the move using the back_up_move method and return
        False. If a move fails for any reason, it returns False, if a move is valid and successful,
        it returns True."""

        #determine if there is a pawn vulnerable to en_passant
        if self._vulnerable != None:
            vuln_flag = True
        else:
            vuln_flag = False

        # store pieces on the square the player is trying to move from
        piece = self._squares[square_1].get_piece()
        piece_2 = self._squares[square_2].get_piece()

        # no action if there is no piece on square_1
        if piece is None:
            return False

        # make sure correct player is moving
        if piece.get_color() != self._turn:
            return False

        # if square_2 is in piece's range, move there
        if self._squares[square_2].get_coords() in piece.get_valid_moves():

            if self._squares[square_2].get_piece() is None:
                #special case for handling pawn en passant vulnerability
                if piece.get_name() == "pawn":
                    if abs(piece.get_position()[1] - self._squares[square_2].get_coords()[1]) > 1:
                        self._vulnerable = piece
                #move
                self._squares[square_1].set_piece(None)
                self._squares[square_2].set_piece(piece)
                piece.set_position(self._squares[square_2].get_coords())
                if piece.get_name() == "pawn":
                    if piece.has_moved == "no":
                        piece.has_moved = "yes"

            else:

                # en_passant
                en_passant = False
                if piece.get_name() == "pawn":
                    if piece_2.get_name() == "pawn":
                        if piece.get_position()[0] == piece_2.get_position()[0]:
                            en_passant = True


                piece_2.set_position((10, 10))
                piece_2.set_status("dead")
                self._squares[square_2].get_piece().clear_valid_moves()
                self._squares[square_1].set_piece(None)
                if en_passant == False:
                    self._squares[square_2].set_piece(piece)
                    piece.set_position(self._squares[square_2].get_coords())
                else:
                    self._squares[square_2].set_piece(None)
                    if piece.get_color() == "white":
                        self.get_square((piece_2.get_position()[0],piece_2.get_position()[1]+1)).set_piece(piece)
                        piece.set_position((piece_2.get_position()[0],piece_2.get_position()[1]+1))
                    else:
                        self.get_square((piece_2.get_position()[0], piece_2.get_position()[1] - 1)).set_piece(piece)
                        piece.set_position((piece_2.get_position()[0], piece_2.get_position()[1] - 1))

                if piece.get_name() == "pawn":
                    if piece.has_moved == "no":
                        piece.has_moved = "yes"
        else:
            return False

        self.refresh_valid_moves()


        # run check checker
        self.check_checker()

        #if it's white's turn, ensure they didn't put self in check, update moves again if black king in check
        if self._turn == "white":
            if self._pieces["white_king"]._check == True:
                self.back_up_move(square_1, square_2, piece, piece_2)
                self.refresh_valid_moves()
                return False
            if self._pieces["black_king"]._check == True:
                self.refresh_valid_moves()

        #same set of checks but for black's turn
        if self._turn == "black":
            if self._pieces["black_king"]._check == True:
                self.back_up_move(square_1, square_2, piece, piece_2)
                self.refresh_valid_moves()
                return False
            if self._pieces["white_king"]._check == True:
                self.refresh_valid_moves()

        #if there was a vulnerable pawn this turn, undo vulnerability
        if vuln_flag:
            self._vulnerable = None

        # switch turn
        if self._turn == "white":
            self._turn = "black"
        else:
            self._turn = "white"

        self.check_game_state()

        self.print_board()
        return True
