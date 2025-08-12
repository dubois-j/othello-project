import numpy as np
from othello.square import Square
from othello.pawn import Pawn
from othello.color import Color

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
        board = np.empty((8,8), dtype=Square)
        
        #Placing center Pawns
        for i in range(8):
            for j in range(8):
                if (i,j)==(4,4) or (i,j)==(3,3):
                    board[i,j] = Square(Pawn(Color.white))
                elif (i,j)==(4,3) or (i,j)==(3,4):
                    board[i,j] = Square(Pawn(Color.black))
                else:
                    board[i,j] = Square(None)

        self.board = board

    
    def addPawn(self, row, col, color):
        """
        If the move is valid, adds a Pawn of given color to the given position.
        """

        # Verifying input validity
        if color not in [0,1]:
            raise ValueError(f"Color must be either 0 or 1 but {color} was given instead.")
        
        if row>7 or row<0 or col>7 or col<0:
            raise ValueError(f"Column and row index must be contained between (0,0) and (7,7) but ({row}, {col}) was given instead.")
        
        # Add Pawn
        if self.canAddPawn(row, col, color):
            self.board[row, col] = Pawn(color)
            self.flipPawns(row, col, color)


    def canAddPawn(self, row, col, color):
        """
        Checks if placing a Pawn on a given Square is a valid move.

        Args:
            row (int):  rown index.
            col (int):  column index.
            color (int):    color of the Pawn to place.
                            O : Black
                            1 : White
        
        Returns:
            (Bool): True if valid move, False otherwise.
        """
        
        if not self.isSquareEmpty(row, col):
            return False
        
        if not self.isFlipPossible(row, col, color):
            return False
        
        return True


    def isSquareEmpty(self, row, col):
        """
        Checks if given Square is empty.

        Args:
            row (int):  row index.
            col (int):  column index.
        
        Returns:
            (Bool): True if Square is empty, False otherwise.
        """

        # Checking if a square is empty
        if self.board[row, col].pawn == None:
            return True
        else:
            return False


    def isFlipPossible(self, row, col, color):
        """
        Checks if placing a Pawn on the Square given by col and row will flip at least one other Pawn.

        Args:
            row (int):  row index
            col (int):  column index
            color (int):    color of the Pawn to place.
                            O : Black
                            1 : White
        
        Returns:
            (Bool): True if at least one Pawn will be flipped, False otherwise.
        """
        
        if row>7 or row<0 or col>7 or col<0:
            raise ValueError(f"Column and row index must be contained between (0,0) and (7,7) but ({row}, {col}) was given instead.")
        
        # Check if can flip direction, stops as soon as flip possible in one direction
        directions = ['N','NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        canFlip = False
        i_dir = 0

        while not canFlip and i_dir < len(directions):
            direction = directions[i_dir]
            increments = self.directionToIndexIncrement(direction)
            current_row, current_col = row + increments[0], col + increments[1]
            stillInBoard = True
            nextIsEmpty = False
            nextIsSameColor = False

            ## First loop, necessary because can't flip on first iteration no matter what
            # Check if not within board
            if not (0 <= current_row <= 7 and 0 <= current_col <= 7):
                stillInBoard = False
            
            # Else, check if next is empty
            elif self.board[current_row, current_col].pawn==None:
                nextIsEmpty = True
            
            # Else, check if next is same color
            elif self.board[current_row, current_col].pawn.color == color:
                nextIsSameColor = True
            

            # Parse direction until done
            while stillInBoard and not nextIsEmpty and not nextIsSameColor and not canFlip:
                current_row, current_col = current_row + increments[0], current_col + increments[1]

                # Check if position is out of board
                if not (0 <= current_row <= 7 and 0 <= current_col <= 7):
                    stillInBoard = False
                
                # Else, check if next is empty
                elif self.board[current_row, current_col].pawn==None:
                    nextIsEmpty = True
                
                # Else, check if next is same color
                elif self.board[current_row, current_col].pawn.color == color:
                    nextIsSameColor = True
                    canFlip = True
            i_dir += 1
            
        return canFlip
    
    def directionToIndexIncrement(self, direction):
        """
        Transforms a direction in ['N','NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'] to a index increment to parse the board.

        Args:
            direction (str): string from ['N','NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        
        Returns:
            (tup): tuple of index increment (row_increment, col_increment)
        """
        
        row_increment, col_increment = 0, 0
        if 'N' in direction:
            row_increment = -1
        if 'S' in direction:
            row_increment = 1
        if 'E' in direction:
            col_increment = 1
        if 'W' in direction:
            col_increment = -1
        
        return (row_increment, col_increment)


    def flipPawns(row, col, color):
        pass


    def displayBoard(self):
        """
        Displays the current state of the board. Black Pawns are displayed as *, white Pawns as O.

        Args:

        Returns:

        """

        pass
    