class Player:
    """
    Player object
    @param color: color fo the player, 0 for black and 1 for white
    @param name: name of the player
    @type color: int
    @type name: str
    """
    def __init__(self,color,name):
        if color!=0 or color!=1:
            raise ValueError(f"Color of Pawn should be 0 for black or 1 for white. The value {color} was given.")
        self.color=color
        self.name=name

    def getMove(self,rownames,colnames):
        """
        Ask the move the player wants to play
        
        Returns:
            (row,col) of the position in the matrix
        """
        inloop=True
        position=input("What position do you want to play").strip()
        while inloop:
            if len(position)==2 and position[0] in colnames and position[1] in rownames:
                row=rownames.index(position[0])
                col=colnames.index(position[1])
                inloop=False
                return (row,col)
            position=input("Invalid position. Please retry:").strip()