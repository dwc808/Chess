class Piece:
    """This class represents a chess Piece. It has child classes to represent specific piece types. It has methods
    to return its private data members for use by the Square and Game classes, as well as methods to set
    them. It also has methods to handle its valid moves."""

    def __init__(self, color, name, position, status):
        """Initializes the piece with color (a string, either 'black' or 'white', a name (string, the specific
        piece it represents), position (the x,y coordinates of the square it is on), status ('alive' or 'dead'), and
        an empty list called _valid_moves, where the coordinates of the squares the piece is allowed to move
        to will be stored."""

        self._color = color
        self._name = name
        self._position = position
        self._status = status
        self._valid_moves = []

    def get_color(self):
        """Returns the color of the piece."""

        return self._color

    def get_name(self):
        """Returns the name of the piece."""

        return self._name

    def get_position(self):
        """Returns the position of the piece."""

        return self._position

    def set_position(self, new_coords):
        """Sets the coorindates of the piece."""
        self._position = new_coords

    def add_valid_move(self, coordinates):
        """Adds the coordinates to the piece's valid moves."""
        self._valid_moves.append(coordinates)

    def get_valid_moves(self):
        """Returns the list of valid moves the piece can currently make."""
        return self._valid_moves

    def clear_valid_moves(self):
        """Clears the list of valid moves the piece can make, used before checking current valid moves."""
        self._valid_moves.clear()

    def set_status(self, status):
        """Sets the status of the piece to the string passed in."""
        self._status = status

    def get_status(self):
        """Returns the piece's current status."""
        return self._status


class King(Piece):
    """This piece represents the King. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the King's valid moves is stored in Game."""

    def __init__(self, color, name, position, status):
        """Initializes the King, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "K"
        else:
            self._icon = "K"
        self._check = False
        self.has_moved = False

    def get_icon(self):
        """Returns the King's icon in the appropriate color."""
        return self._icon

    def in_check(self):
        """Returns True if in Check, False otherwise"""
        return self._check

    def get_moved(self):
        """Returns True if piece has been moved, False otherwise."""
        return self.has_moved


class Castle(Piece):
    """This piece represents the Castle. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the Castle's valid moves is stored in Game."""

    def __init__(self, color, name, position, status):
        """Initializes the Castle, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "C"
        else:
            self._icon = "C"
        self.has_moved = False

    def get_icon(self):
        """Returns the Castle's icon in the appropriate color."""
        return self._icon

    def get_moved(self):
        """Returns True if piece has been moved, False otherwise."""
        return self.has_moved

class Bishop(Piece):
    """"This piece represents the Bishop. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the Bishop's valid moves is stored in Game."""

    def __init__(self, color, name, position, status):
        """Initializes the Bishop, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "B"
        else:
            self._icon = "B"

    def get_icon(self):
        """Returns the Bishop's icon in the appropriate color."""
        return self._icon


class Knight(Piece):
    """"This piece represents the Knight. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the Bishop's valid moves is stored in Game."""

    def __init__(self, color, name, position, status):
        """Initializes the Knight, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "k"
        else:
            self._icon = "k"

    def get_icon(self):
        """Returns the Knight's icon in the appropriate color."""
        return self._icon

class Queen(Piece):
    """"This piece represents the Queen. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the Queen's valid moves is stored in Game."""

    def __init__(self, color, name, position, status):
        """Initializes the Queen, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "Q"
        else:
            self._icon = "Q"

    def get_icon(self):
        """Returns the Queen's icon in the appropriate color."""
        return self._icon


class Pawn(Piece):
    """"This piece represents the Pawn. It has all of the piece data members and methods, plus a new data member,
    icon, and a method to retrieve it. This is used solely for updating the status of the board. A specific
    method for assessing the Bishop's valid moves is stored in Pawn."""

    def __init__(self, color, name, position, status):
        """Initializes the Pawn, giving it the appropriate icon based on its color."""
        super().__init__(color, name, position, status)
        if self._color == "white":
            self._icon = "P"
        else:
            self._icon = "P"

        self.has_moved = "no"

    def get_icon(self):
        """Returns the Pawn's icon in the appropriate color."""
        return self._icon

    def get_moved(self):
        """Returns 'yes' if pawn has moved, 'no' otherwise."""
        return self.has_moved