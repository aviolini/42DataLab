from beverages import HotBeverage
import random

class CoffeeMachine:
	def __init__(self):
		self.__drink = 0
		self.__fixed = False
		random.seed()
	class EmptyCup(HotBeverage):
		def __init__(self):
			super().__init__()
			self.name = "empty cup"
			self.price = 0.9
			self.descr = "An empty cup?! Gimme my money back!"
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	def repair(self):
		self.__drink = 0
		self.__fixed = True
	def serve(self, *args):
		if not self.__fixed and self.__drink == 10:
			raise self.BrokenMachineException()
		mylist = [self.EmptyCup(), args[0]]
		choice = random.randrange(0,2)
		ret = mylist[choice]
		if not self.__fixed and choice == 1:
			self.__drink += 1
		return ret



	
	

