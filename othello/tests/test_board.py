import sys
sys.path.append("/home/julien.dubois@Digital-Grenoble.local/Documents/POO/othello-project/")

from othello.board import Board
from othello.color import Color

# Possible pawn to play from initial position
def display_board(myBoard, showPossibleMoves=True):
    print("  A B C D E F G H")
    for i in range(8):
        print(f"{i} ", end="")
        for j in range(8):
            if myBoard.canAddPawn(i,j,Color.black):
                if showPossibleMoves :
                    print("B ", end="")
                else:
                    print("- ", end="")
            elif myBoard.canAddPawn(i,j,Color.white):
                if showPossibleMoves :
                    print("W ", end="")
                else:
                    print("- ", end="")
            else:
                if myBoard.board[i,j].pawn==None:
                    print("- ", end="")
                elif myBoard.board[i,j].pawn.color==Color.black:
                    print("\u25CB ", end="")
                elif myBoard.board[i,j].pawn.color==Color.white:
                    print("\u25CF ", end="")
        print()

myBoard = Board()
myBoard.displayBoard()
#print(myBoard.getPossibleMoves(Color.black))
#display_board(myBoard)
myBoard.addPawn(2,3,Color.black)
myBoard.displayBoard()
#display_board(myBoard)
myBoard.addPawn(2,2,Color.white)
myBoard.displayBoard()
#display_board(myBoard)
myBoard.addPawn(4,5,Color.black)
myBoard.displayBoard()
#display_board(myBoard)
