from othello.player import Player  
from othello.color import Color
from othello.board import Board

class Othello:

    def __init__(self):
        """
        
        """

        name0 = input("Nom du joueur 0 (pions noirs): ")
        name1 = input("Nom du joueur (pions blancs) : ")
        
        self.playerBlack = Player(Color.black,name0)
        self.playerWhite = Player(Color.white,name1)
        self.current_turn = self.playerBlack # Le joueur qui commence
    
        self.scores = {self.playerBlack: 2, self.playerWhite: 2} # Score initial
        self.board = Board()
        

    def get_score(self):
        """
        
        """

        black_score = 0
        white_score = 0
        for row in range(8):
            for col in range(8):
                pawn = self.board.board[row, col].pawn
                if pawn is not None:
                    if pawn.color == 0:
                        black_score += 1
                    else:
                        white_score += 1
                """# arajouter   
                else pawn is None :
                 gannant +=1
                """        
        return {'black': black_score, 'white': white_score}
    
                          
    def get_winner(self):
        """
        
        """

        points = self.score()
        if points['black'] > points['white']:
            return self.playerBlack.name
        elif points['white'] > points['black']:
            return self.playerWhite.name
        else:
            return "Match nul"                    
        
        
    def is_gameOver(self):
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
        print(f"Gagnant : {self.get_winner()}")