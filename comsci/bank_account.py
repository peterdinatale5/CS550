class Account:
		#constructor - defines the properties and gives them initial values
	def __init__(self, name):
		self.name = name
		self.account = 123
		self.balance = 1000

	def transaction(self):
		trans = str(input("do you want deposit or withdrawl? (d/l)").lower())
		if trans == "d":
			dep = int(input("how much money do you want to deposit? "))
			self.balance += dep
			print(self.balance)
		if trans == "l":
			wit = int(input("how much money do you want to withdrawl? "))
			self.balance -= wit
			print(self.balance)

name = "peter"
Peter = Account(name)
Nate = Account("Nate")

Peter.transaction()