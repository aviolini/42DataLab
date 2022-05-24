import numpy as np

def myprint(x, *y):
  print ('----',x,'-----------')
  for v in y:
    print (v, "\n")

#1
myprint(1, np.zeros(5, dtype=int))

#2
myprint(2, np.ones(10, dtype=int))

#3
myprint(3, np.arange(10,51, dtype=int ))

#4
myprint(4, np.arange(10,51,2, dtype=int))

#5
myprint(5, np.eye(3,3, dtype=int))

#6
myprint(6, np.random.rand(1)[0])

#7
myprint(7, np.linspace(0.,1.,10))