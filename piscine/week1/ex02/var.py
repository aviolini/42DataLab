
def my_print(x):
	print (x,"has a type",type(x))

def my_var():
	a=42
	my_print(a)
	a="42"
	my_print(a)
	a="quarante-deux"
	my_print(a)
	a=42.0
	my_print(a)
	a=True
	my_print(a)
	a=[42]
	my_print(a)
	a={42:42}
	my_print(a)
	a=(42,)
	my_print(a)
	a=set()
	my_print(a)

my_var()

