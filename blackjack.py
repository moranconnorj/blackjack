from random import shuffle


class Deck:
	"""A Class for creating a new deck of cards"""

	def __init__(self):
		"""initializes the new Deck object, which is an empty list"""
		self.game_deck = [(x, y) for x in range(4) for y in range(1, 14)]

	def shuffle(self):
		"""shuffles deck into random order"""
		shuffle(self.game_deck)

	def draw_card(self):
		"""pulls out the n items out of game_deck"""
		pull = self.game_deck.pop(-1)
		return pull
		#pull = self.game_deck[-num:]
		#del self.game_deck[-num:]
		#return pull

	def cards_left(self):
		"""returns the length of game_deck"""
		return len(self.game_deck)

	def sort_deck(self):
		"""sorts the list of tuples back to the order it was initialized to"""
		self.game_deck.sort()



def test():
	def Deck_test():
		#__init__ test
		deck = Deck()
		assert deck.game_deck[0] == (0, 1)
		assert len(deck.game_deck) == 52
		#shuffle test
		deck1 = Deck()
		assert deck.game_deck == deck1.game_deck
		deck1.shuffle()
		assert deck.game_deck != deck1.game_deck
		#draw_card test
		assert deck.draw_card() == (3, 13)
		assert len(deck.game_deck) == 51
		#cards_left test
		assert deck.cards_left() == 51
		assert deck1.cards_left() == 52
		#sort test
		deck1.sort_deck()
		assert deck1.game_deck[0] == (0, 1) and deck1.game_deck[-1] == (3, 13)

	def Card_test():
		pass
	Deck_test()
	Card_test()



if __name__ == "__main__":
	test()



