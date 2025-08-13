from othello.color import Color
class Player:
    """
    Player object
    @param color: color fo the player, 0 for black and 1 for white
    @param name: name of the player
    @type color: int
    @type name: str
    """
    def __init__(self,color:Color,name):
        if not isinstance(color,Color):
            raise ValueError(f"Color of Player should be Color.black or Color.white. \"{color}\" was given.")
        self.__color=color
        self.__name=name
    @property
    def color(self):
        return self.__color
    @property
    def name(self):
        return self.__name
    
    def getMove(self,rownames,colnames,possibleMoves):
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
                if (row,col) in possibleMoves:
                    inloop=False
                    return (row,col)
                else:
                    position=input("Move not possible. Please retry: ").strip()
            else:
                position=input("Invalid position. Please retry: ").strip()