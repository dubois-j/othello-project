class Pawn:
    """
    Define a pawn, 0 for black, 1 for white

    """
    def __init__(self,color):
        """
        Args:
            color: 0 or 1
        """
        if color!=0 and color!=1:
            raise ValueError(f"Color of Pawn should be 0 for black or 1 for white. The value {color} was given.")
        self.color=color
    
    def flip(self):
        """
        flip the pawn to the other color
        """
        if self.color==1:
            self.color=0
        else:
            self.color=1