import sys
sys.path.append("/home/julien.dubois@Digital-Grenoble.local/Documents/POO/othello-project/")

from othello.board import Board
from othello.color import Color
from othello.ai_player_alphabeta import AIPlayerAlphaBeta

myAIPlayer = AIPlayerAlphaBeta(Color.black, 'myAI')