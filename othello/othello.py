from player import Player  

class Othello:
    def __init__(self):
        
        name0 = input("Nom du joueur 0 (pions noirs): ")
        name1 = input("Nom du joueur (pions blancs) : ")
        
        self.playerBlack = Player(0,name0)
        self.playerWhite = Player(0,name1)
        self.current_turn = self.player0 # Le joueur qui commence
    
        self.scores = {self.playerBlack: 2, self.playerWhite: 2} # Score initial
        self.board = Board()
        
    def get_score(self):
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
        return {0: black_score, 1: white_score}
    
                
                          
    def get_winner(self):
        points = self.score()
        if points[0] > points[1]:
            return self.name0
        elif points[1] > points[0]:
            return self.name1
        else:
            return "Match nul"                    
        
        
    
        
    def is_gameOver(self):
        scores = self.get_score()
        total = scores[0] + scores[1]
        return total == 64 #plateau complet    
    def position(self, row, col):
        pass
    def currrent_player(self):
        return self.current_turn
    def play(self, row, col):
        
        if self.board.canAddPawn(row, col, self.current_turn):
           self.board.addPawn(row, col, self.current_turn)
           
        else:
            print("Coup invalide, veuillez réessayer.")
        
        
    def show_result(self):
        
        print("\n--- Résultat ---")
        print(f"{self.playerBlack.name} (Noirs) : {self.scores[self.playerBlack]} points")
        print(f"{self.playerWhite.name} (Blancs) : {self.scores[self.playerWhite]} points")
        print(f"Gagnant : {self.get_winner()}")

    



            