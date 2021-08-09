from board  import board
from deck   import deck
from dice   import dice
from player import player

class game:
	def __init__(self, player_count, difficulty):
		self.player_count = player_count
		self.difficulty = difficulty

		new_board = board()
		new_deck = deck()
		new_dice = dice()
		new_board.draw_board()

		ai_players = []
		human = player()

		while len(ai_players) < (int(player_count) - 1):
			ai_players.append(player())