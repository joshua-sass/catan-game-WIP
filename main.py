#imports here
from game import game
from board import board
from tile import tile
from piece import piece
from deck import deck

if __name__ == "__main__":
	print("MAKE LOGO HERE")
	#draw main screen

	#player number (fills out with ai)
	# - 2 to 5 total players
	# type number and press enter. check input
	print("What is your player numer")
	players = int(input())
	if players.isnumeric() != True:
		pass
		#ask for input again

	#offer difficulty selection
	# - easy, ai makes decision based on top 5 options, memory buffer of 1 round
	# - medium, ai makes decision based on top 3 options, memory buffer of 3 rounds
	# - hard, ai makes decision based on best option, memory buffer is all cards in hands
	# type selection and press enter. check input
	difficulies = ["easy", "medium", "hard"]
	diff = input()
	while not diff in difficulties:
		palyers = input()

	#credits and tools used
	#press enter to continue or type rules for rulebook (can use browser to open webpage)

	#create game object and begin
	new_game = game(players, diff)
	new_game.initiliaze()