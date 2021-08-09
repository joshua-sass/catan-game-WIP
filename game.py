class game:
	def __init__(self, player_count, difficulty):
		self.player_count = player_count
		self.difficulty = difficulty

	def initiliaze(self):
		new_board = board()
		new_board.draw_board()		