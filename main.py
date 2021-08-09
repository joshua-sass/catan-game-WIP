#imports here
from game import game
from board import board
#from tile import tile
#from piece import piece
#from deck import deck

if __name__ == "__main__":
	difficulties = ["easy", "medium", "hard"]
	MAX_PLAYERS = 5
	numbers_of_players = [player for player in range(1+1, MAX_PLAYERS+1)]
	print("MAKE LOGO HERE")
	#draw main screen

	#player number (fills out with ai)
	# - 2 to 5 total players
	# type number and press enter. check input
	print("What is your number of players?")
	players = int(input())
	while not players in numbers_of_players:
		print("You must have made a mistake! Try again.")
		players = int(input())

	#offer difficulty selection
	# - easy, ai makes decision based on top 5 options, memory buffer of 1 round
	# - medium, ai makes decision based on top 3 options, memory buffer of 3 rounds
	# - hard, ai makes decision based on best option, memory buffer is all cards in hands
	# type selection and press enter. check input

	print("What is your difficulty?")
	diff = input().lower()
	while not diff in difficulties:
		print("You must have made a mistake! Try again.")
		diff = input().lower()

	#credits and tools used
	#press enter to continue or type rules for rulebook (can use browser to open webpage)

	#create game object and begin
	new_game = game(players, diff)
	new_game.initiliaze()