import sys
sys.path.append("/home/thibault.launois@Digital-Grenoble.local/Documents/othello-project/")

from othello.player import Player
from othello.pawn import Pawn
from othello.square import Square

rownames=[1,2,3,4,5,6,7,8]
colnames=['A','B','C','D','E','F','G','H']

julien=Pawn(0)
print(julien.color)
julien.flip()
print(julien.color)
"""
a,b=julien.getMove(rownames,colnames)
print(f"The position is {a} and {b}")
"""

