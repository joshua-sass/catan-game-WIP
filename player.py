from pieces import pieces

class player:
	def __init__(self, id):
		self.new_pieces = pieces()
		self.get_points()

	def place_piece(self, connection):
		pass

	def replace_piece(self, connection):
		pass

	def get_points(self):
		points_moving = self.new_pieces.player_pieces
		points_total = 0

		for iterator in range(0,9): #25 pieces but only first 9 are worth points
			if iterator < 4 and points_moving[iterator] == 1:
				points_total += 1
			if iterator > 3 and points_moving[iterator] == 1:
				points_total += 2

		return points_total