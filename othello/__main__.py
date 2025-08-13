import othello.board as Board
import othello.player as Player
import othello.othello as Othello
from othello.color import Color
from square import Square


julien=Square()


game=Othello()

while not game.isGameOver():

    # Player Black
    # Vérifier si ya des coups possibles
    currentMove = game.playerBlack.getMove(game.board.rownames, 
                                           game.board.colnames)
    currentAvailableMoves = game.board.getPossibleMoves(Color.black)
    while currentMove not in currentAvailableMoves:
        print("T'es con ou quoi ?")
        currentMove = game.playerBlack.getMove(game.board.rownames, 
                                           game.board.colnames)
    
    # Player White
    game.play() # Utiliser board.addPawn() plutôt

game.showResults()

