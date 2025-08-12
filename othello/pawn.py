from othello.color import Color

class Pawn:
    """
    Define a pawn, 0 for black, 1 for white

    """
    def __init__(self,color:Color):
        """
        Args:
            color: 0 or 1
        """
        if not isinstance(color,Color):
            raise ValueError(f"Color of Pawn should be Color.black or Color.white. \"{color}\" was given.")
        self.__color=color

    @property
    def color(self):
        return self.__color
    
    def flip(self):
        """
        flip the pawn to the other color
        """
        if self.__color==Color.black:
            self.__color=Color.white
        else:
            self.__color=Color.black