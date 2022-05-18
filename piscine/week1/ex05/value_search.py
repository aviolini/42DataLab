
import sys

if len(sys.argv) != 2:
	print(quit())

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

d={}
for ks in states:
	for kcc in capital_cities:
		if states[ks] == kcc:
			d[ks]=capital_cities[kcc]
for k in d:
	if d[k] == sys.argv[1]:
		print (k)
		print (quit())
print('Unknown state')



