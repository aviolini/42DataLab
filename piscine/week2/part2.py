import numpy as np
import matplotlib.pyplot as plt

def myprint(x, *y):
  print ('----',x,'-----------')
  for v in y:
    print (v, "\n")

#1
myprint (1, np.random.randint(10, size=(2,3)))

#2
myprint (2, np.arange(0,12, dtype=int).reshape(4,3))

#3
def createArr(x):
  return np.linspace(0.,1.,x).reshape(1,x)
n = 10
arr = createArr(n)
myprint(3, arr, arr.shape)

#4
arr = np.random.randint(100, size=(10,12))
myprint (4, arr, arr[0:4,8:12])

#5
m = 5
n = 5
arr = np.empty((0,n))
for i in range(m):
    arr = np.vstack((arr, createArr(n)))
myprint(5, arr)
plt.imshow(arr)
plt.show()

#6
arr2 = np.random.randint(10, size=(m,n))
print(arr.shape, arr2.shape)
ret = np.matmul(arr, arr2)
myprint(6, arr, arr2, ret)
plt.imshow(ret)
plt.show()