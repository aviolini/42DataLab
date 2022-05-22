class HotBeverage:
	def __init__(self):
		self.name = "hot beverage"
		self.price = 0.3
		self.descr = "Just some hot water in a cup."
	def description(self):
		return self.descr
	def __str__(self):
		return f"name: {self.name}\nprice: " + "{:.2f}".format(self.price) + f"\ndescription: {self.description()}"

class Coffee(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "coffee"
		self.price = 0.4
		self.descr = "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "tea"

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "chocolate"
		self.price = 0.5
		self.descr = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "cappuccino"
		self.price = 0.45
		self.descr = "Un po' di Italia nella sua tazza!"
