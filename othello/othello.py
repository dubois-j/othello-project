from player import Player  

class Othello:
    def __init__(self):
        
        name0 = input("Nom du joueur 0 (pions noirs): ")
        name1 = input("Nom du joueur (pions blancs) : ")
        
        self.player0 = Player(0,name0)
        self.player1 = Player(0,name1)
        self.current_turn = self.player0 # Le joueur qui commence
    
        self.scores = {self.player0: 2, self.player1: 2} # Score initial
        
    
    def get_winner(self):
        
        if self.scores[self.player0] > self.scores[self.player1]:
            return self.name1
        elif self.scores[self.player1] > self.scores[self.player0]:
            return self.name2
        else:
            return "Match nul"

    
    def is_gameOver(self):
        pass
    
    def position(self, row, col):
        pass
    def currrent_player(self):
        return self.current_turn
    def play():
        #mettre le pion 
        #self.board
        #sinon au prochain
        pass
    
    def show_result(self):
        
        print("\n--- Résultat ---")
        print(f"{self.name0} (Noirs) : {self.scores[self.player0]} points")
        print(f"{self.name1} (Blancs) : {self.scores[self.player1]} points")
        print(f"Gagnant : {self.get_winner()}")

    



            