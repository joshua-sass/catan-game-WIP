from random import randint

class dice:
	def __init__(self):
		#idk man its a dice
		sides = 6

	def roll(self):
		return randint(0, sides)