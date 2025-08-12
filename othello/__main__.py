import othello.board as board
import othello.player as player
import othello.othello as othello

game=othello()

while not game.isGameOver():
    othello.play()

game.showResults()

