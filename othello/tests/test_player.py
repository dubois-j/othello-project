import sys
sys.path.append("/home/thibault.launois@Digital-Grenoble.local/Documents/othello-project")
from othello.player import Player
from othello.pawn import Pawn
from othello.square import Square
from othello.color import Color

rownames=[1,2,3,4,5,6,7,8]
colnames=['A','B','C','D','E','F','G','H']

julien=Player(Color.white,"Julien")
julien.color=Color.black
"""
a,b=julien.getMove(rownames,colnames)
print(f"The position is {a} and {b}")
"""

