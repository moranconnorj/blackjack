from random import shuffle

class Card:
	
	""" Class for a single card from a deck of 52 cards. Cards are passed in as a tuple
	in the format (suit, rank), and assigned a value according to the rules of blackjack.
	Arguments
	-----------
	card_input : tuple
		cards are passed in as a tuple in the format (suit, rank)
	Parameters
	-----------
	value : int
		card is assigned integer value from function get_value()
	__str__ : built in overload
	"""
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	ranks = ["N/a", "Ace", "2", "3", "4", "5", "6", "7", "8", 
			"9", "10", "Jack", "Queen", "King"]

	def __init__(self, card_input):
		self.suit = card_input[0]
		self.rank = card_input[1]
		self.value = self.get_value()

	def __str__(self):
		return self.ranks[self.rank] + " of " + self.suits[self.suit]

	def get_rank(self):
		return self.ranks[self.rank]

	def get_value(self):
		"""assigns value to card ranks based on blackjack rules"""
		#FIX ACE START VALUE ????
		if self.rank > 10: #Ace value is 1 by defualt, addressed in Player class check_ace()
			return 10
		else:
			return int(self.rank)

class Deck:
	"""Class for creating a new deck of cards in tuples in the format of (suit, rank)
	Parameters
	-----------
	game_deck : tuple
		a list of 52 tuple pairs is initialized and assigned to game_deck
	__str__ : built in overload

	"""

	def __init__(self):
		
		self.game_deck = [Card((x, y)) for x in range(4) for y in range(1, 14)]

	def __str__(self):
		s = ""
		for i in range(len(self.game_deck)):
			s = s + str(self.game_deck[i]) + "\n"
		return s

	def shuffle(self):
		"""shuffles deck into random order"""
		shuffle(self.game_deck)

	def draw_card(self):
		"""removes last card from game_deck and returns it"""
		return self.game_deck.pop(-1)

	def cards_left(self):
		"""returns the length of game_deck"""
		return len(self.game_deck)

	def sort_deck(self): # not working with Card class method
		"""sorts the list of tuples back to the order it was initialized to"""
		self.game_deck.sort()
	

def test():
	def Deck_test():
		deck = Deck()
		assert len(deck.game_deck) == 52

	def Card_test():
		five = Card((1, 5))
		king = Card((1,13))
		ace = Card((2,1))
		assert five.value == 5
		assert king.value == 10
		assert ace.value == 1
		assert str(five) == "5 of Diamonds"

	Deck_test()
	Card_test()


