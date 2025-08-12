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
        board[3,3].pawn, board[4,4].pawn = Pawn(1), Pawn(1)
        board[3,4].pawn, board[4,3].pawn = Pawn(0), Pawn(0)

        self.board = board

    
    def addPawn(self, row, col, color):
        """
        If the move is valid, adds a Pawn of given color to the given position.
        """

        if self.canAddPawn(col, row, color):
            self.board[row, col] = Pawn(color)
            self.flipPawns(row, col, color)


    def canAddPawn(self, row, col, color):
        pass


    def isSquareEmpty(self, row, col):
        pass


    def isFlipPossible(self, row, col, color):
        """
        Checks if placing a Pawn on the Square given by col and row will flip at least one other Pawn.

        Args:
            col (int): column index
            row (int): row index
            color (int): color of the Pawn to place.
                         O : Black
                         1 : White
        
        Returns:
            (Bool): True if at least one Pawn will be flipped, False otherwise.
        """

        pass
    

    def flipPawns(row, col, color):



    def displayBoard(self):
        """
        Displays the current state of the board. Black Pawns are displayed as *, white Pawns as O.

        Args:

        Returns:

        """

    