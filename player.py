from deck import Card, Deck

class Player:
	""" """
	def __init__(self, deck):
		self.deck = deck
		self.hand = []
		self.mxscore = 21

	def __str__(self):
		s = [c.get_rank() for c in self.hand]
		return ", ".join(s)

	def get_card(self):
		"""gets card from deck and puts it into hand"""
		self.hand.append(self.deck.draw_card())

	def score(self):
		"""returns score of current hand"""
		soft = False
		t = sum([card.value for card in self.hand])
		if any(card.rank == 1 for card in self.hand) and (t + 10 <= self.mxscore): # allows for ace value to be 1 or 11
			soft = True
			return (t + 10)
		else:
			return (t)


class User(Player):
	"""Subclass of Player class with input to determine if User should hit"""
	def hit(self):
		"""asks users input and calls get_card() if user inputs to Hit"""
		hitstay = raw_input("Hit or Stay?\n")
		if hitstay == "Hit":
			self.get_card()
			return True
		elif hitstay == "Stay":
			return False
		else:
			print("Incorrect input, must match string")
			self.hit()

class Dealer(Player):
	"""Subclass of Player class with logic to determine if Dealer should hit"""

	def hit(self):
		"""calls get_card() depending on dealers current score"""
		if self.score() < 17:
			self.get_card()
			return True
		else:
			return False

	def first_ace(self):
		"""if dealers first card is an Ace, correctly shows the value of 11"""
		if self.hand[0].rank == 1:
			return 11
		else:
			return self.hand[0].value

def test():
	def player_test():
		player = User(Deck())
		player.get_card()
		player.get_card()
		player.get_card()
		assert len(player.hand) == 3
		assert str(player.hand[0]) == 'King of Spades'
		#assert player.score() == 30
		player2 = Player(Deck())
		player2.hand = [Card((1,1)), Card((2,1)), Card((3,1))]
	player_test()


test()



