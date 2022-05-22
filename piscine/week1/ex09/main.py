from beverages import *
from machine import *
import random

random.seed()
machine = CoffeeMachine()
beverages = [Coffee(), Tea(), Chocolate(), Cappuccino()]

for x in range (2):
	try:
		nDrinks = 0
		for n in range(30):
			ret = machine.serve(random.choice(beverages))
			if type(ret) != type(machine.EmptyCup()):
				nDrinks += 1
				print ('n drinks:', nDrinks)
			print (ret, "\n")
	except CoffeeMachine.BrokenMachineException as e:
		print ('EXCEPTION:', e, "\n")
	machine.repair()
