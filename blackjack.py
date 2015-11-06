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
		def deal(self):
			self.user.get_card()
			self.user.get_card()
			self.dealer.get_card()
			print("\nDealer has {0} ??? for a visible total of {1} points".format(str(self.dealer), self.dealer.first_ace()))
			self.dealer.get_card() # Dealer gets 2nd card after first print to keep 2nd card hidden
			print("You have {0} for a total of {1} points".format(str(self.user), self.user.score()))
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			check_blackjack(self)

		def check_blackjack(self):
			if self.dealer.score() == 21:
				print("Dealer has {0} for a total of {1} points".format(str(self.dealer), self.dealer.score()))
				print("Dealer got a Blackjack! You Lose!")
			elif self.user.score() == 21:
				print("You got a Blackjack! You Win!")
			else:
				user_hit(self)

		def user_hit(self):
			while self.user.score() <= 21 and self.user.hit():
				if self.user.score() > 21:
					print("You have {0} for a total of {1} points. \nYOU BUSTED!".format(str(self.user), self.user.score()))
				if self.user.score() <= 21:
					print("You have {0} for a total of {1} points.".format(str(self.user), self.user.score()))
			if self.user.score() <= 21:
				print("You stay with {0} for a total of {1} points.".format(str(self.user), self.user.score()))
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				dealer_hit(self)
				
		def dealer_hit(self):
			print("Dealer has {0} for a total of {1} points.".format(str(self.dealer), self.dealer.score()))
			if self.dealer.score() >= 17:
				print("Dealer stays at {0}".format(self.dealer.score()))
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				compare_score(self)
			while self.dealer.score() < 17:
				print("Dealer Hits")
				self.dealer.hit()
				print("Dealer has {0} for a total of {1} points.".format(str(self.dealer), self.dealer.score()))
				if 17 <= self.dealer.score() <= 21:
					print("Dealer stays at {0}".format(self.dealer.score()))
					print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					compare_score(self)
				elif self.dealer.score() > 21:
					print("DEALER BUSTED!".format(str(self.dealer), self.dealer.score()))

		def compare_score(self):
			if self.user.score <= self.dealer.score:
				print("The Dealer's {0} beats your {1}. \nYOU LOSE!").format(self.dealer.score(), self.user.score())
			if self.user.score > self.dealer.score:
				print("Your {0} beats the Dealer's {1}. \nYOU WIN!").format(self.user.score(), self.dealer.score())
				
		deal(self)		
				
				
				

				
					# if self.dealer.score() <= 21:
					# 	print("Dealer Hits")
					# 	print("Dealer has {0} for a total of {1} points.".format(str(self.dealer), self.dealer.score()))
					# else:
					# 	print("Dealer has {0} for a total of {1} points. DEALER BUSTED!".format(str(self.dealer), self.dealer.score()))
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



