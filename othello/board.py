import numpy as np
from square import Square
from pawn import Pawn

class Board:
    rownames = (1, 2, 3, 4, 5, 6, 7, 8)
    colnames = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    def __init__(self):
        """
        Intialise the board as a 8x8 numpy array of Squares. All but the 4 center Squares are empty.
        The D5 and E4 Squares are initialised with a black Pawn, and the D4 and E5 Squares with a
        white Pawn.

            A   B   C   D   E   F   G   H
        1   
        2
        3
        4               O   *
        5               *   O
        6
        7
        8

        Args:
        
        Returns:

        """

        # Creating empty board
        board = np.repeat(Square(None))
        board = np.reshape(board, (8,8))

        # Placing center Pawns
        board[3,3], board[4,4] = Square(Pawn(1))
        board[3,4], board[4,3] = Square(Pawn(0))

        self.board = board