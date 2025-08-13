from othello.player import Player  
from othello.color import Color
from othello.board import Board

class Othello:

    def __init__(self):
        """
        Constructor of Class Othello
        Attributes:
            playerBlack (Player)
            playerWhite (Player)
            currentPlayer (Player)
            scores (dict)
            board (Board)
        """

        name0 = input("Nom du joueur 0 (pions noirs): ")
        name1 = input("Nom du joueur (pions blancs) : ")
        
        self.playerBlack = Player(Color.black,name0)
        self.playerWhite = Player(Color.white,name1)
        self.currentPlayer = self.playerBlack # Le joueur qui commence
    
        self.scores = {self.playerBlack: 2, self.playerWhite: 2} # Score initial
        self.board = Board()
        

    def getScore(self):
        """
        Computes the current score. 
        If the game is over and there is no tie, also add empty squares to the winner's score.

        Returns:
            (dict): Score as a dictionary, with self.playerBlack and self.playerWhite as keys.
        """

        black_score = 0
        white_score = 0
        empty = 0
        for row in range(8):
            for col in range(8):
                pawn = self.board.board[row, col].pawn
                if pawn is not None:
                    if pawn.color == 0:
                        black_score += 1
                    else:
                        white_score += 1
                else:
                    emmpty +=1

        if self.isGameOver():
            if black_score > white_score:
                black_score += empty
            
            elif white_score > black_score:
                white_score += empty
                     
        return {self.playerBlack: black_score, 
                self.playerWhite: white_score}
    

    def updateScore(self):
        """
        Updates the game's current score.
        """

        self.scores = self.getScore()
    
                          
    def getWinner(self):
        """
        Compute and return the name of the winner, or 'tie' if there's a tie.

        Returns:
            (str): Name of the winner, or "Tie" if there is no winner.
        """

        if self.scores[self.playerBlack] > self.scores[self.playerWhite]:
            return self.playerBlack.name
        elif self.scores[self.playerBlack] < self.scores[self.playerWhite]:
            return self.playerWhite.name
        else:
            return "Match nul"                    
        
        
    def isGameOver(self):
        """
        Checks if there are possible moves left. If yes, the game is not over, else, the game is over.

        Args:

        Returns:
            (Bool): True if there are valid moves avaible, False otherwise.
        """

        possibleMovesBlack = self.board.board.getPossibleMoves(Color.black)
        possibleMovesWhite = self.board.board.getPossibleMoves(Color.white)

        if len(possibleMovesBlack)==0 and len(possibleMovesWhite==0):
            return True
        
        return False


    def position(self, row, col):
        """
        
        """

        pass


    def currrent_player(self):
        """
        
        """

        return self.current_turn
    

    def play(self, row, col):
        """
        
        """

        if self.board.canAddPawn(row, col, self.current_turn.color):
           self.board.addPawn(row, col, self.current_turn.color)
           
        else:
            print("Coup invalide, veuillez réessayer.")
        
        
    def show_result(self):
        """
        
        """

        print("\n--- Résultat ---")
        print(f"{self.playerBlack.name} (Noirs) : {self.scores[self.playerBlack]} points")
        print(f"{self.playerWhite.name} (Blancs) : {self.scores[self.playerWhite]} points")
        print(f"Gagnant : {self.getWinner()}")