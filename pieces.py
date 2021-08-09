class pieces:
	def __init__(self):
		player_1_pieces = []
		player_2_pieces = []
		player_3_pieces = []
		player_4_pieces = []

		#first 4 are cities
		#next 5 are houses
		#final 15 are roads

		for iterator in range(0, 25): #are pieces in play
			player_1_pieces.append(0)
			player_2_pieces.append(0)
			player_3_pieces.append(0)
			player_4_pieces.append(0)
