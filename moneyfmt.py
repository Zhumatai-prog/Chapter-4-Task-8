# def dollarize(x):
#     d = '${:,.2f}'.format(x)
#     print(d)


# class MoneyFmt():
# 	def __init__(self, money):
# 		self.money = money

# 	def update(self, new_money):
# 		self.money = new_money
# 		return str(self.dollarize(self.money))

# 	def __repr__(self):
# 		return f"{self.money}"

# 	def __str__(self):
# 		return str(self.dollarize(self.money))

# 	def dollarize(self, x):
# 		self.d = '${:,.2f}'.format(x)
# 		return self.d




class MoneyFmt():
	def __init__(self, money):
		self.money = money

	def update(self, new_money):
		self.money = new_money
		

	def __repr__(self):
		self.a = str(self.money).split("$")
		print(self.a[0])
		return self.a[0]

	def __str__(self):
		self.d = '${:,.2f}'.format(self.money)
		return self.d






