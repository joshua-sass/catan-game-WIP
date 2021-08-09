from tile import tile
from random import randint

class board:
	def __init__(self):
		#determine tiles and values here!
		self.chits = []
		self.harbors = ["s", "?", "?", "b", "?", "w", "g", "?", "r"]
		self.tiles = []
		#d = desert
		#w = wood
		#r = rock
		#g = grain
		#s = sheep
		#b = brick

	def generate_chit_values(self): #(tuning these values) #potentially revisit this section to make code cleaner
		grain_values = []
		wood_values = []
		pasture_values = []
		rock_values = []
		brick_values = []

		self.chits = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
		moving_chits = self.chits

		while len(moving_chits) > 3:
			temp = randint(0, len(moving_chits)-1)
			grain_values.append(moving_chits[temp])
			moving_chits.remove(moving_chits[temp])

			temp = randint(0, len(moving_chits)-1)
			wood_values.append(moving_chits[temp])
			moving_chits.remove(moving_chits[temp])

			temp = randint(0, len(moving_chits)-1)
			pasture_values.append(moving_chits[temp])
			moving_chits.remove(moving_chits[temp])

			temp = randint(0, len(moving_chits)-1)
			rock_values.append(moving_chits[temp])
			moving_chits.remove(moving_chits[temp])

			temp = randint(0, len(moving_chits)-1)
			brick_values.append(moving_chits[temp])
			moving_chits.remove(moving_chits[temp])

		temp = randint(0, len(moving_chits)-1)
		grain_values.append(moving_chits[temp])
		moving_chits.remove(moving_chits[temp])

		temp = randint(0, len(moving_chits)-1)
		wood_values.append(moving_chits[temp])
		moving_chits.remove(moving_chits[temp])

		temp = randint(0, len(moving_chits)-1)
		pasture_values.append(moving_chits[temp])
		moving_chits.remove(moving_chits[temp])

		for iterator in range(0, 3):

			self.tiles.append(tuple(["g", grain_values[iterator]]))
			self.tiles.append(tuple(["w", wood_values[iterator]]))
			self.tiles.append(tuple(["s", pasture_values[iterator]]))
			self.tiles.append(tuple(["r", rock_values[iterator]]))
			self.tiles.append(tuple(["b", brick_values[iterator]]))

		for chit in range(0,1):
			print(len(self.tiles))
			self.tiles.append(tuple(["g", grain_values[3]]))
			self.tiles.append(tuple(["w", wood_values[3]]))
			self.tiles.append(tuple(["s", pasture_values[3]]))

		#print(self.tiles)
		#print(len(self.tiles))

	def draw_board(self):
		answer = "n"

		while answer != "y":
			self.generate_board()
			print("Does this board look satisfactory? (y,n)")
			answer = input().lower()
			if answer == "y":
				break
			print("Okay! Let's try again")


	def generate_board(self):

		self.tiles = []
		desert_tile = tuple(["d", 0])
		self.tiles.append(desert_tile)

		self.generate_chit_values()
		self.tiles.sort()
		print(self.tiles)
		#numeric system so tiles can be stored in an array (tile #x is always in y location)