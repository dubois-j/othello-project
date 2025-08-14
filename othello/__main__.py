#import othello.board as Board
#import othello.player as Player
from othello.othello import Othello
#from othello.color import Color
#from square import Square
from othello.ai_player_minimax import AIPlayerMiniMax
import time

game=Othello()


while not game.isGameOver():
    
    game.board.updateBoard(game.currentPlayer.name, game.currentPlayer.color, showPossibleMoves=True, colorToShowMoves=game.currentPlayer.color)
    currentAvailableMoves = game.board.getPossibleMoves(game.currentPlayer.color)
    if len(currentAvailableMoves)>0: # Vérifier si ya des coups possibles
        (row,col)=game.currentPlayer.getMove(game.board.rownames,
                                       game.board.colnames,
                                       currentAvailableMoves)
        game.board.addPawn(row,col,game.currentPlayer.color)
        game.updateScore()
    game.nextPlayer()

game.board.updateBoard()
game.showResult()

