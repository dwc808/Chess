class Square:
    """This class represents a square on the chess board. Each square stores information about itself
    that can be used by various methods of the Game and Piece classes, primarily for printing and moving
    pieces. It also stores any Piece objects that are currently on the square."""

    def __init__(self, name, coords, color):
        """Initializes the name, coordinates, and color of the square, setting them to the values passed.
        _piece is always initialized as None. Name should be a two character string such as 'a1', coordinates
        should be a tuple of two integers representing x and y coordinates, and color should be a string, either
        'black' or 'white'."""

        self._name = name
        self._coords = coords
        self._color = color
        self._piece = None

    def get_name(self):
        """Returns the square's name."""

        return self._name

    def get_coords(self):
        """Returns the square's coordinates (x,y) as a tuple."""

        return self._coords

    def get_color(self):
        """Returns the color of the square."""

        return self._color

    def get_piece(self):
        """Returns None if no piece is present, otherwise returns the piece object on the square."""

        return self._piece

    def set_piece(self, piece_object):
        """Update the _piece data member."""

        self._piece = piece_object

    def is_empty(self):
        """Returns True if the square is empty, False if a piece is present."""

        if self._piece == None:
            return True
        else:
            return False