# How do class objects work?

class PiggyBank(object):
	def __init__(self, balance):
		super(PiggyBank, self).__init__()
		self.balance = balance

	def addBalance(self, amount):
		self.balance += amount

	def subtractBalance(self, amount):
		self.balance -= amount



bank = PiggyBank(100)

bank.subtractBalance(70)
print bank.balance
bank.addBalance(75)
print bank.balance