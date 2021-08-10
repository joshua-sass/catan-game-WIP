from tile import tile
from random import randint
import numpy

class board:
	def __init__(self):
		#determine tiles and values here!
		self.chits = []
		self.harbors = []
		self.tiles = []
		self.connections = []
		#d = desert
		#w = wood
		#r = rock
		#g = grain
		#s = sheep
		#b = brick
		self.initiate_connections()
		self.draw_board()

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

			self.tiles.append(tuple(["g", grain_values[3]]))
			self.tiles.append(tuple(["w", wood_values[3]]))
			self.tiles.append(tuple(["s", pasture_values[3]]))

		self.tiles.sort()

	def generate_harbor_values(self):
		harbor_vals = ["s", "?", "?", "b", "?", "w", "g", "?", "r"]
		harbor_locs = [x for x in range(0,9)]
		numpy.random.shuffle(harbor_vals)

		for x in range(0,9):
			self.harbors.append(tuple([harbor_vals[x],harbor_locs[x]]))

		#self.harbors.sort()

	def draw_board(self):
		answer = "n"

		while answer != "y":
			self.generate_board()
			print("Does this board look satisfactory? (y,n)")
			answer = input().lower()
			if answer == "y":
				break
			print("Okay! Let's try again")

	def initiate_connections(self):
		moving_conn = []
		#connections between tiles
		moving_conn.append(tuple(["1", "2"]))
		moving_conn.append(tuple(["2", "3"]))
		moving_conn.append(tuple(["3", "7"]))
		moving_conn.append(tuple(["3", "6", "7"]))
		moving_conn.append(tuple(["2", "3", "6"]))
		moving_conn.append(tuple(["2", "5", "6"]))
		moving_conn.append(tuple(["1", "2", "5"]))
		moving_conn.append(tuple(["1", "4", "5"]))
		moving_conn.append(tuple(["1", "4"]))
		moving_conn.append(tuple(["4", "8"]))
		moving_conn.append(tuple(["4", "8", "9"]))
		moving_conn.append(tuple(["4", "5", "9"]))
		moving_conn.append(tuple(["5", "6", "10"]))
		moving_conn.append(tuple(["6", "7", "11"]))
		moving_conn.append(tuple(["7", "12"]))
		moving_conn.append(tuple(["7", "11", "12"]))
		moving_conn.append(tuple(["6", "10", "11"]))
		moving_conn.append(tuple(["5", "9", "10"]))
		moving_conn.append(tuple(["8", "13"]))
		moving_conn.append(tuple(["8", "9", "13"]))
		moving_conn.append(tuple(["9", "13", "14"]))
		moving_conn.append(tuple(["9", "10", "14"]))
		moving_conn.append(tuple(["10", "14", "15"]))
		moving_conn.append(tuple(["10", "11", "15"]))
		moving_conn.append(tuple(["11", "15", "16"]))
		moving_conn.append(tuple(["11", "12", "16"]))
		moving_conn.append(tuple(["12", "16"]))
		moving_conn.append(tuple(["13", "17"]))
		moving_conn.append(tuple(["13", "14", "17"]))
		moving_conn.append(tuple(["14", "17", "18"]))
		moving_conn.append(tuple(["14", "15", "18"]))
		moving_conn.append(tuple(["15", "18", "19"]))
		moving_conn.append(tuple(["15", "16", "19"]))
		moving_conn.append(tuple(["16", "19"]))
		moving_conn.append(tuple(["17", "18"]))
		moving_conn.append(tuple(["18", "19"]))
		#connections between tile + edge
		moving_conn.append(tuple(["1", "NW"]))
		moving_conn.append(tuple(["1", "N"]))
		moving_conn.append(tuple(["2", "N"]))
		moving_conn.append(tuple(["3", "N"]))
		moving_conn.append(tuple(["3", "NE"]))
		moving_conn.append(tuple(["7", "NE"]))
		moving_conn.append(tuple(["12", "NE"]))
		moving_conn.append(tuple(["12", "SE"]))
		moving_conn.append(tuple(["16", "SE"]))
		moving_conn.append(tuple(["19", "SE"]))
		moving_conn.append(tuple(["19", "S"]))
		moving_conn.append(tuple(["18", "S"]))
		moving_conn.append(tuple(["17", "S"]))
		moving_conn.append(tuple(["17", "SW"]))
		moving_conn.append(tuple(["13", "SW"]))
		moving_conn.append(tuple(["8", "NW"]))
		moving_conn.append(tuple(["8", "SW"]))
		moving_conn.append(tuple(["4", "NW"]))
		#this might be a bit yucky, consider revising

		self.connections.extend(moving_conn)

	def generate_board(self):

		self.tiles = []
		desert_tile = tuple(["d", 0])
		self.tiles.append(desert_tile)

		self.generate_chit_values()
		print(self.tiles)

		self.generate_harbor_values()
		print(self.harbors)
		#numeric system so tiles can be stored in an array (tile #x is always in y location)