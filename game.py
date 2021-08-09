from board  import board
from deck   import deck
from dice   import dice
from player import player

class game:
	def __init__(self, player_count, difficulty):
		self.player_count = player_count
		self.difficulty = difficulty

		self.new_board = board()
		self.new_deck = deck()
		self.new_dice = dice()
		self.new_board.draw_board()

		self.ai_players = []
		self.human = player()

		while len(self.ai_players) < (int(self.player_count) - 1):
			self.ai_players.append(player())