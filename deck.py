from random import randint

class deck:

	def __init__(self):
		self.cards = [] 
		#25 total development cards
		for card in range(0,14):#0  - 13 knights
			self.cards.append("knight")
		self.cards.append("monopoly")
		self.cards.append("monopoly")#14 - 15 monopoly
		self.cards.append("road building")
		self.cards.append("road building")#16 - 17 road building
		self.cards.append("year of plenty")
		self.cards.append("year of plenty")#18 - 19 year of plenty
		for card in range(20,25):#20 - 24 victory point
			self.cards.append("victory point")

	def no_cards(self):
		pass #see if i need to write this condition bc i might have to make tuples or another class haha :)
		
	def draw_card(self):
		if len(self.cards) > 0:
			card_number = randint(0,len(self.cards)-1)
		else:
			no_cards()
		chosen_card = self.cards[card_number]
		self.cards.pop(card_number)
		return chosen_card