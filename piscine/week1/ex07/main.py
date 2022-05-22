from intern import Intern

noname = Intern()
mark = Intern('Mark')
print('noname:\t', noname.__str__())
print('mark:\t', mark.__str__())
coffee = noname.makecoffee()
print('coffee:\t', coffee.__str__())
try:
	noname.work()
except Exception as e:
	print ('noname:\t', e)
try:
	mark.work()
except Exception as e:
	print ('mark:\t', e)
