from othello.player import Player
import random
import time

class AIPlayerRandom(Player):
    def getMove(self, rownames, colnames, possibleMoves):
        print("Random player turn.")
        #time.sleep(0.5)
        return possibleMoves[random.randrange(len(possibleMoves))]