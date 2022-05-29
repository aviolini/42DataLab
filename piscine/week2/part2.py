import numpy as np
import matplotlib.pyplot as plt

x = 1
def myprint(*y):
  global x
  print ('\n----',x,'-----------')
  for v in y:
    print (v, "\n")
  x += 1

#1
# myprint (np.random.randint(10, size=(2,3)))
mu, sigma = 0, 0.1 # mean and standard deviation
arr = np.random.normal(mu, sigma, 100)
myprint (arr)
count, bins, ignored = plt.hist(arr, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()

#2
myprint (np.arange(0,12, dtype=int).reshape(4,3))

#3
def createArr(x):
  return np.linspace(0.,1.,x).reshape(1,x)

n = 10
arr = createArr(n)
myprint(arr, arr.shape)

#4
arr = np.random.randint(100, size=(10,12))
myprint (arr, arr[0:4,8:12])

#5
m = 331
n = 188
arr = np.empty((0,n))
for i in range(m):
    arr = np.vstack((arr, createArr(n)))
myprint(arr)
plt.imshow(arr)
plt.show()

#6
import requests

myprint()

print('myMatrix')
plt.imshow(arr)
plt.show()

print('myPicture')
response = requests.get("https://static.wikia.nocookie.net/telletubbies/images/e/e5/Tinky_Winky.jpg/revision/latest?cb=20200317005814").content
with open('/content/pic1.jpg', 'wb') as handle:
    handle.write(response)
img = (plt.imread('/content/pic1.jpg'))
plt.imshow(img)
plt.show()
print('size of myMatrix:', arr.shape)
print('size of myPicture:', img.shape)
print('myMatrix x myPicture')
ret = np.matmul(arr, img)
# myprint(6, arr, img, ret)
plt.imshow((ret* 255).astype(np.uint8))
plt.show()