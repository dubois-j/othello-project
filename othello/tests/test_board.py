import sys
sys.path.append("/home/julien.dubois@Digital-Grenoble.local/Documents/POO/othello-project/")

from othello.board import Board

myBoard = Board()

# for i in range(8):
#    for j in range(8):
#        print(myBoard.board[i,j])

#print(myBoard.isSquareEmpty(3,3))

# Possible pawn to play from initial position
for i in range(8):
    for j in range(8):
        if myBoard.canAddPawn(i,j,0):
            print("B ", end="")
        elif myBoard.canAddPawn(i,j,1):
            print("W ", end="")
        else:
            if myBoard.board[i,j].pawn==None:
                print("- ", end="")
            elif myBoard.board[i,j].pawn.color==0:
                print("◯ ", end="")
            elif myBoard.board[i,j].pawn.color==1:
                print("⬤ ", end="")
    print()
#print(myBoard.board[0,0].pawn.color)
