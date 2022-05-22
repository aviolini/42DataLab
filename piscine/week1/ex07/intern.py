
class Intern:
	def __init__(self, *args):
		if len(args) == 1:
			self.name="My name? I'm " + args[0] + "."
		else:
			self.name= "My name? I’m nobody, an intern, I have no name."
	def __str__(self):
		return self.name
	class Coffee:
		def __init__(self):
			self.namex="This is the worst coffee you ever tasted."
		def __str__(self):
			return self.namex
		def na(self):
			return self.namex
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	def makecoffee(self):
		return self.Coffee()
