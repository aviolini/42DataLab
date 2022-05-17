import sys
try:
	if (len(sys.argv) != 3):
		raise NameError
	ret = (float(sys.argv[1]) + float(sys.argv[2]))
	if ret % 1 == 0:
		ret = int(ret)
	print (ret)
except NameError:
	print('Error: wrong number of arguments!')
except ValueError:
	print('Error: no valid number!')


