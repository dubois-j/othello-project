import numpy as np
from othello.square import Square
from othello.pawn import Pawn
from othello.color import Color
import matplotlib.pyplot as plt
import time

class Board:
    rownames = ('1', '2', '3', '4', '5', '6', '7', '8')
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
        self.initBoard()

    
    def addPawn(self, row, col, color, printWrongInput=False):
        """
        If the move is valid, adds a Pawn of given color to the given position.
        """

        # Verifying input validity
        if color not in [Color.black, Color.white]:
            raise ValueError(f"Color must be either Color.white or Color.black but {color} was given instead.")
        
        if row>7 or row<0 or col>7 or col<0:
            raise ValueError(f"Column and row index must be contained between (0,0) and (7,7) but ({row}, {col}) was given instead.")
        
        # Add Pawn
        if self.canAddPawn(row, col, color):
            self.board[row, col].addPawn(color)
            self.flipPawns(row, col, color)

        elif printWrongInput:
            print("Coup non valide ! Pas bien.")


    def canAddPawn(self, row, col, color):
        """
        Checks if placing a Pawn on a given Square is a valid move.

        Args:
            row (int):  rown index.
            col (int):  column index.
            color (Color):    color of the Pawn to place.
        
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


    def flipPawns(self, row, col, color):
        """
        Flip the pawns on the board after having placed a pawn of a given color on a given square.

        Args:
            row (int):  row index
            col (int):  column index
            color (Color):    color of the Pawn to place.
        
        Returns:

        """

        # Check and flip possible pawns in all directions
        for direction in ['N','NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
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
            while stillInBoard and not nextIsEmpty and not nextIsSameColor:
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
                    current_row, current_col = current_row - increments[0], current_col - increments[1]
                    while (current_row, current_col) != (row, col):
                        self.board[current_row, current_col].pawn.flip()
                        current_row, current_col = current_row - increments[0], current_col - increments[1]


    def getPossibleMoves(self, color:Color):
        """
        Parse the board and obtains the list of possible move for a given Color.

        Args:
            color (Color): object of class Color. Either Color.white or Color.black.
        
        Returns:
            possibleMoves (list): list of coordinates (as tuples) of possible moves.
        """

        possibleMoves = []
        for i in range(8):
            for j in range(8):
                if self.canAddPawn(i,j,color):
                    possibleMoves.append((i,j))
        
        return possibleMoves


    def initBoard(self):
        """
        Initialize the figure object of Board

        Args:

        Returns:

        """
        plt.ion()

        self.fig = plt.figure(figsize=(8,8))
        self.ax = self.fig.add_subplot(111)
        
        
    
    def updateBoard(self, playerName, playerColor, showPossibleMoves = False, colorToShowMoves = None):
        """
        Displays the current state of the board. Black Pawns are displayed as *, white Pawns as O.

        Args:

        Returns:

        """
        self.ax.cla()
        #Drawing the board of the othello
        self.ax.set_ylim(-0.5,7.5)
        self.ax.set_xlim(-0.5,7.5)
        self.ax.set_facecolor("darkolivegreen")
        self.ax.set_yticks([7,6,5,4,3,2,1,0],['1','2','3','4','5','6','7','8'])
        self.ax.set_xticks([0,1,2,3,4,5,6,7],['A','B','C','D','E','F','G','H'])
        self.ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True)
        self.ax.tick_params(axis="y", right=True, left=True, labelright=True, labelleft=True)
        if playerColor==Color.black:
            self.ax.set_title(f"{playerName}, it's your turn with black pawn", weight='bold')
        elif playerColor==Color.white:
            self.ax.set_title(f"{playerName}, it's your turn with white pawn", weight='bold')
        for i in [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]:
            self.ax.axvline(i,color='k')
            self.ax.axhline(i,color='k')
        
        if showPossibleMoves:
            if not isinstance(colorToShowMoves, Color):
                raise TypeError(f"Expected Class Color in 'colorToShowMoves' but were given {type(colorToShowMoves)} instead.")
            else:
                self.updateBoardColor(colorToShowMoves,possible=True)

        self.updateBoardColor(Color.black)
        self.updateBoardColor(Color.white)

    def updateBoardColor(self,color, possible=False):
        x=[]
        y=[]
        
        for i in range(8):
            for j in range(8):
                if self.board[i,j].isEmpty():
                    if possible:
                        if (i,j) in self.getPossibleMoves(color):
                            x.append(j)
                            y.append(7-i)
                elif self.board[i,j].pawn.color==color and possible==False:
                    x.append(j)
                    y.append(7-i)
        if possible:
            if color==Color.black:
                self.ax.plot(x,y,c='k',markersize=45, marker='o',linestyle='',alpha=0.25)
            elif color==Color.white:
                self.ax.plot(x,y,c='w',markersize=45, marker='o',linestyle='',alpha=0.25)
        elif color==Color.black:
            self.ax.plot(x,y,c='k',markersize=45, marker='o',linestyle='')
        elif color==Color.white:
            self.ax.plot(x,y,c='w',markersize=45, marker='o',linestyle='')