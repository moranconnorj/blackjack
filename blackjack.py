from deck import Card, Deck
from player import Player, User, Dealer


class Round:
	"""start a round of blackjack
	Arguments
	----------
	deck : shared deck of cards between classes
	Parameters
	----------
	user : player class controlled by input
	dealer : player class controlled by hit rules
	mxscore : maximum score without busting
	"""
	def __init__(self, deck):
		self.deck = deck
		self.user = User(deck)
		self.dealer = Dealer(deck)
		self.mxscore = 21
		self.deck.shuffle()

	def play(self):

		if self.deck.game_deck:
			self.user.get_card()
			self.user.get_card()
			self.dealer.get_card()
			print("\nDealer has {0} ??? for a visible total of {1} points".format(str(self.dealer), self.dealer.first_ace()))
			self.dealer.get_card() # Dealer gets 2nd card after first print to keep 2nd card hidden
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("You have {0} for a total of {1} points".format(str(self.user), self.user.score()))
			if self.dealer.score() == 21:
				print("Dealer got a Blackjack! You Lose!")
			if self.user.score() == 21:
				print("You got a Blackjack! You Win!")
			while self.user.score() < 21 and self.user.hit():
				if self.user.score() > 21:
					print("You have {0} for a total of {1} points. YOU BUSTED!".format(str(self.user), self.user.score()))
				else:
					print("You have {0} for a total of {1} points.".format(str(self.user), self.user.score()))
			print("Dealer has {0} for a total of {1} points.".format(str(self.dealer), self.dealer.score()))
			while self.dealer.hit():
				if self.dealer.score() > 21:
					print("Dealer has {0} for a total of {1} points. DEALER BUSTED!".format(str(self.dealer), self.dealer.score()))


class Blackjack:
	"""holds multiple rounds of blackjack"""
	def __init__(self):
		pass

def test():
	def round_test():
		player = Round(Deck())
		player.play()
	round_test()



if __name__ == "__main__":
	test()



