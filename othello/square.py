import pawn as pa
class Square:
    """A square on the board to contain None or a PAwn object"""
    def __init__(self,pawn):
        if pawn==None or isinstance(pawn,pa.Pawn):
            self.pawn=pawn
        else:
            raise AttributeError("You didn't gave a None or Pawn object to Square.")