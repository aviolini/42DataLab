import sys
try:
	if (len(sys.argv) != 4):
		raise NameError	
	ret = ((int(sys.argv[1])) * 60 * 60) + ((int(sys.argv[2])) * 60) + int(sys.argv[3])
	print (ret)
except NameError:
	print('Error: wrong number of arguments!')
except ValueError:
	print('Error: no valid number!')


