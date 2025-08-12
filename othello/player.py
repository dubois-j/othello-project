class Player:
    """
    Player object
    @param color: color fo the player, 0 for black and 1 for white
    @param name: name of the player
    @type color: int
    @type name: str
    """
    def __init__(self,color,name):
        if color!=0 and color!=1:
            raise ValueError(f"Color of Pawn should be 0 for black or 1 for white. The value {color} was given.")
        self.__color=color
        self.__name=name
    @property
    def color(self):
        return self.__color
    @property
    def name(self):
        return self.__name
    
    def getMove(self,rownames,colnames):
        """
        Ask the move the player wants to play
        Args:
            rownames:list of row names on board
            colnames: list of col names on board
        Returns:
            (row,col) of the position in the matrix
        """
        inloop=True
        position=input("What position do you want to play ? ").strip()
        while inloop:
            if len(position)==2 and position[0] in colnames and int(position[1]) in rownames:
                row=rownames.index(int(position[1]))
                col=colnames.index(position[0])
                inloop=False
                return (row,col)
            position=input("Invalid position. Please retry: ").strip()