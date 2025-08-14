from othello.player import Player  
from othello.color import Color
from othello.board import Board
from othello.ai_player_alphabeta import AIPlayerAlphaBeta
from othello.ai_player_minimax import AIPlayerMiniMax
from othello.ai_player_random import AIPlayerRandom

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
        self.initPlayers()
        self.currentPlayer = self.playerBlack # Le joueur qui commence
    
        self.scores = {self.playerBlack: 2, self.playerWhite: 2} # Score initial
        self.board = Board()
        
    def initPlayers(self):
        """
        Ask if players should be human or AI.
        Attribute the correct player object to attribute playerblack and player white

        Args:

        Returns:

        """
        print("Players can be either human or AI.")
        self.choosePlayer(Color.black)
        self.choosePlayer(Color.white)
    
    def choosePlayer(self,color):
        """
        Ask name if human, ask which AI if not
        """
        yes=['y','yes','o','oui']
        no=['non','no','n']
        if color==Color.black:
            color_str="black"
        elif color==Color.white:
            color_str="white"
        else:
            raise TypeError("choosePlayer did not receive a color object.")
        
        answer=input(f"Should player {color_str} be human ? (y/n)").strip().lower()
        while answer not in yes and answer not in no:
            answer=input("Incorrect input. Please retry: ").strip().lower()
        
        if answer in yes:
            name = input(f"Name of {color_str} player: ")
            player=Player(color,name)
        elif answer in no:
            list_ai=["minimax","alphabeta","random","1","2","3"]
            ai=input("Which type of AI ? (1:minimax 2:alphabeta 3:random) ").strip().lower()
            while ai not in list_ai:
                ai=input("Incorrect input. Please retry: ").strip().lower()
            if ai=='minimax' or ai=='1':
                player=AIPlayerMiniMax(color,"Minimax")
            elif ai=='alphabeta' or ai=='2':
                player=AIPlayerAlphaBeta(color,"Minimax")
            else:
                player=AIPlayerRandom(color,"Random")
        if color==Color.black:
            self.playerBlack=player
        elif color==Color.white:
            self.playerWhite=player


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
                    if pawn.color == Color.black:
                        black_score += 1
                    else:
                        white_score += 1
                else:
                    empty +=1

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

        possibleMovesBlack = self.board.getPossibleMoves(Color.black)
        possibleMovesWhite = self.board.getPossibleMoves(Color.white)

        if len(possibleMovesBlack)==0 and len(possibleMovesWhite)==0:
            return True
        
        return False


    def nextPlayer(self):
        """
        Update self.currentPlayer to the next Player.
        """

        if self.currentPlayer == self.playerBlack:
            self.currentPlayer = self.playerWhite
        else:
            self.currentPlayer = self.playerBlack

        
    def showResult(self):
        """
        
        """

        print("\n--- Résultat ---")
        print(f"{self.playerBlack.name} (Noirs) : {self.scores[self.playerBlack]} points")
        print(f"{self.playerWhite.name} (Blancs) : {self.scores[self.playerWhite]} points")
        print(f"Gagnant : {self.getWinner()}")


    def copy(self):
        game = Othello()