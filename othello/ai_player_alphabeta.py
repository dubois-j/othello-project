from othello.player import Player
from othello.board import Board
from othello.othello import Othello

class AIPlayerAlphaBeta(Player):

    def __init__(self, color, name):
        """
        Constructor of Class AIPlayerAlphaBeta. 
        Inherits from Class Player; has an additional attribute 'depth'.
        """

        super().__init__(color, name)
        self.depth = self.getDepth()


    def getDepth(self):
        """
        Asks the user to input a depth until the input is valid.

        Args:

        Returns:
            (int):  depth input by the user as an integer.
        """

        depth = input("Enter the wanted depth within of the AI Alpha Beta Player:").strip()
        while not self.isDepthCorrectFormat(depth):
            depth = input("Wrong input. Please enter the wanted depth of the AI (for example: 3)\t").strip()
        return int(depth)


    def isDepthCorrectFormat(self, depth):
        """
        Checks if the depth given is valid.

        Args:
            depth (str): depth given as a string.
        
        Returns:
            (Bool): True if depth given is valid, False otherwise.
        """

        if depth in [str(i) for i in range(100)]:
            return True
        return False
    

    def applyAlphaBeta(self, game:Othello, currentDepth:int, alpha=-999999, beta=999999):
        """
        
        """

        if game.isGameOver() or currentDepth<=0:
            return self.getWinningScore(game)

        if self.isMyTurn(game):
            for move in game.board.getPossibleMoves(self.color):
                gameCopy = game.copy()
                gameCopy.board.addPawn(move[0], move[1], self.color)
                gameCopy.updateScore()
                score = self.applyAlphaBeta(gameCopy, currentDepth-1, alpha, beta)
                if score > alpha:
                    alpha = score
                    bestMove = move
                    if alpha >= beta:
                        break
            return alpha
        else:
            for move in game.board.getPossibleMoves(self.color):
                gameCopy = game.copy()
                gameCopy.board.addPawn(move[0], move[1], self.color)
                


        else:
            pass


    def isMyTurn(self, game):
        """
        Checks if it's the AI turn or the oppononent's one.

        Arg:
            game (Othello): current state of the game
        
        Returns:
            (Bool): True if it's the AI turn, False if it's the opponent's turn.
        """
        
        if game.currentPlayer() == self:
            return True
        
        return False