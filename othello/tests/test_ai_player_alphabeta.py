import sys


sys.path.append("/home/julien.dubois@Digital-Grenoble.local/Documents/POO/othello-project/")

from othello.color import Color
from othello.ai_player_alphabeta import AIPlayerAlphaBeta
from othello.othello import Othello
from othello.player import Player
from othello.board import Board

board = Board()
# myAIPlayer1 = AIPlayerAlphaBeta(Color.black, 'myAI')
# playerWhite = Player(Color.white, 'Julien')
# game = Othello(init=False, playerBlack=myAIPlayer1, playerWhite=playerWhite, board=board)


# copiedGame = game.copy()
# copiedGame.board.addPawn(3, 2, Color.black)
# copiedGame.board.displayBoard()
# game.board.displayBoard()

copiedBoard = board.copy()
board.addPawn(3,2,Color.black)
board.displayBoard()
#print(board.board)
copiedBoard.displayBoard()
#print(copiedBoard.board)