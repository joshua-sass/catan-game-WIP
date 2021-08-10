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

		self.board_string_by_line = []

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
			#d = desert
			#w = wood
			#r = rock
			#g = grain
			#s = sheep
			#b = brick

			self.tiles.append(tuple(["g", str(grain_values[iterator])]))
			self.tiles.append(tuple(["w", str(wood_values[iterator])]))
			self.tiles.append(tuple(["s", str(pasture_values[iterator])]))
			self.tiles.append(tuple(["r", str(rock_values[iterator])]))
			self.tiles.append(tuple(["b", str(brick_values[iterator])]))

		for chit in range(0,1):

			self.tiles.append(tuple(["g", str(grain_values[3])]))
			self.tiles.append(tuple(["w", str(wood_values[3])]))
			self.tiles.append(tuple(["s", str(pasture_values[3])]))

		numpy.random.shuffle(self.tiles)

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

	def default_board_draw(self):
		temp = []
		temp.append("_________________________________________________________________________________________________________________________")
		temp.append("|                                                                                                                        |")
		temp.append("|                                          /\\    /\\    /\\                                                                |")
		temp.append("|                                         /  \\  /  \\  /  \\                                                               |")
		temp.append("|                                        /(1) \\/(2) \\/(3) \\                                                              |")
		temp.append("|                                        | " +self.tiles[0][0]+self.tiles[0][1].zfill(2)+ "|| " +self.tiles[1][0]+self.tiles[1][1].zfill(2)+ "|| " +self.tiles[2][0]+self.tiles[2][1].zfill(2)+ "|                                                              |")
		temp.append("|                                       /\\    /\\    /\\    /\\                                                             |")
		temp.append("|                                      /  \\  /  \\  /  \\  /  \\                                                            |")
		temp.append("|                                     /(4) \\/(5) \\/(6) \\/(7) \\                                                           |")
		temp.append("|                                     | " +self.tiles[3][0]+self.tiles[3][1].zfill(2)+ "|| " +self.tiles[4][0]+self.tiles[4][1].zfill(2)+ "|| " +self.tiles[5][0]+self.tiles[5][1].zfill(2)+ "|| " +self.tiles[6][0]+self.tiles[6][1].zfill(2)+ "|                                                           |")
		temp.append("|                                    /\\    /\\    /\\    /\\    /\\                                                          |")
		temp.append("|                                   /  \\  /  \\  /  \\  /  \\  /  \\                                                         |")
		temp.append("|                                  /(8) \\/(9) \\/(10)\\/(11)\\/(12)\\                                                        |")
		temp.append("|                                  | " +self.tiles[7][0]+self.tiles[7][1].zfill(2)+ "|| " +self.tiles[8][0]+self.tiles[8][1].zfill(2)+ "|| " +self.tiles[9][0]+self.tiles[9][1].zfill(2)+ "|| " +self.tiles[10][0]+self.tiles[10][1].zfill(2)+ "|| " +self.tiles[11][0]+self.tiles[11][1].zfill(2)+ "|                                                        |")
		temp.append("|                                  \\    /\\    /\\    /\\    /\\    /                                                        |")
		temp.append("|                                   \\  /  \\  /  \\  /  \\  /  \\  /                                                         |")
		temp.append("|                                    \\/(13)\\/(14)\\/(15)\\/(16)\\/                                                          |")
		temp.append("|                                     | " +self.tiles[12][0]+self.tiles[12][1].zfill(2)+ "|| " +self.tiles[13][0]+self.tiles[13][1].zfill(2)+ "|| " +self.tiles[14][0]+self.tiles[14][1].zfill(2)+ "|| " +self.tiles[15][0]+self.tiles[15][1].zfill(2)+ "|                                                           |")
		temp.append("|                                     \\    /\\    /\\    /\\    /                                                           |")
		temp.append("|                                      \\  /  \\  /  \\  /  \\  /                                                            |")
		temp.append("|                                       \\/(17)\\/(18)\\/(19)\\/                                                             |")
		temp.append("|                                        | " +self.tiles[16][0]+self.tiles[16][1].zfill(2)+ "|| " +self.tiles[17][0]+self.tiles[17][1].zfill(2)+ "|| " +self.tiles[18][0]+self.tiles[18][1].zfill(2)+ "|                                                              |")
		temp.append("|                                        \\    /\\    /\\    /                                                              |")
		temp.append("|                                         \\  /  \\  /  \\  /                                                               |")
		temp.append("|                                          \\/    \\/    \\/                                                                |")
		temp.append("|                                                                                                                        |")
		temp.append("|     Tiles have their number put in ()s. The resource given is represented by the char followed by the number required  |")
		temp.append("|     to be rolled. For example, w06 represents wood when rolling 6. To claim a spot for building, represent them with   |")
		temp.append("|     a space. For example, city 1 2 5, would represent the building of a city at the triangulation of tile 1,2 and 5.   |")
		temp.append("|     For tiles with only two neighbors, those two tile numbers are sufficient so city 1 2. When only one neighbor is    |")
		temp.append("|     present, cardinal directions will be used, so for example city 3 NE.                                               |")
		temp.append("|                                                                                                                        |")																														
		temp.append("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

		return temp		

	def generate_board(self):

		self.tiles = []
		desert_tile = tuple(["d", "7"])
		self.tiles.append(desert_tile)

		self.generate_chit_values()
		self.generate_harbor_values()
		#numeric system so tiles can be stored in an array (tile #x is always in y location)

		self.board_string_by_line = self.default_board_draw()
		for line in self.board_string_by_line:
			print(line)
		#time to draw the board in console