import player as pl
import pawn as pa
import square as sq

rownames=[1,2,3,4,5,6,7,8]
colnames=['A','B','C','D','E','F','G','H']

julien=pa.Pawn(0)
print(julien.color)
julien.flip()
print(julien.color)
"""
a,b=julien.getMove(rownames,colnames)
print(f"The position is {a} and {b}")
"""

