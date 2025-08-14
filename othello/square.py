from othello.pawn import Pawn

class Square:

    """
    A square on the board to contain None or a PAwn object
    """
    def __init__(self,pawn=None):
        if pawn==None or isinstance(pawn,Pawn):
            self.__pawn=pawn
        else:
            raise AttributeError("You didn't gave a None or Pawn object to Square.")
        
    @property
    def pawn(self):
        """
        
        """

        return self.__pawn
    
    def addPawn(self,color):
        """
        
        """

        self.__pawn=Pawn(color)
    
    def isEmpty(self):
        """
        
        """

        return self.__pawn==None
    
    def isFull(self):
        """
        
        """

        return not self.isEmpty(self)