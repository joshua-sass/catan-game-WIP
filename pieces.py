class pieces:
	def __init__(self):
		self.player_pieces = []

		#first 4 are cities
		#next 5 are houses
		#final 15 are roads

		for iterator in range(0, 25): #are pieces in play
			self.player_pieces.append(0)