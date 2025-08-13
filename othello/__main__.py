#import othello.board as Board
#import othello.player as Player
from othello.othello import Othello
#from othello.color import Color
#from square import Square

game=Othello()

while not game.isGameOver():
    game.board.displayBoard(showPossibleMoves=True, colorToShowMoves=game.currentPlayer.color)
    currentAvailableMoves = game.board.getPossibleMoves(game.currentPlayer.color)
    if len(currentAvailableMoves)>0: # Vérifier si ya des coups possibles
        (row,col)=game.currentPlayer.getMove(game.board.rownames,
                                       game.board.colnames,
                                       currentAvailableMoves)
        game.board.addPawn(row,col,game.currentPlayer.color)
        game.updateScore()
        #game.board.displayBoard(showPossibleMoves=True, colorToShowMoves=game.currentPlayer.color)
    game.nextPlayer()

game.board.displayBoard()
game.showResult()

