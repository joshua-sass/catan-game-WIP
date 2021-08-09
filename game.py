from board import board
from pieces import pieces
from deck import deck
from dice import dice

class game:
	def __init__(self, player_count, difficulty):
		self.player_count = player_count
		self.difficulty = difficulty

		new_board = board()
		new_pieces = pieces()
		new_deck = deck()
		new_dice = dice()
		new_board.draw_board()				