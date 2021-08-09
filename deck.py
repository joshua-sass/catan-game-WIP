from random import randint

class deck:

	def __init__(self):
		cards = [] 
		#25 total development cards
		for card in range(0,14):#0  - 13 knights
			cards.append("knight")
		cards.append("monopoly")
		cards.append("monopoly")#14 - 15 monopoly
		cards.append("road building")
		cards.append("road building")#16 - 17 road building
		cards.append("year of plenty")
		cards.append("year of plenty")#18 - 19 year of plenty
		for card in range(20,25):#20 - 24 victory point
			cards.append("victory point")

	def no_cards(self):
		pass #see if i need to write this condition bc i might have to make tuples or another class haha :)
		
	def draw_card(self):
		if len(cards) > 0:
			card_number = randint(0,len(cards)-1)
		else:
			no_cards()
		chosen_card = cards[card_number]
		cards.pop(card_number)
		return chosen_card