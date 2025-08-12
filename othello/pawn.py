class pawn:
    def __init__(self,color):
        if color!=0 or color!=1:
            raise ValueError(f"Color of Pawn should be 0 for black or 1 for white. The value {color} was given.")
        self.color=color
    
    def flip(self):
        if self.color==1:
            self.color=0
        else:
            self.color=1