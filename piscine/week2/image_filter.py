# https://www.big-meter.com/opensource/en/5fec9fc796d0a3317c75c0f3.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.rgb_to_hsv.html
# plt al posto di cv2
# mettere altri filtri
# problema astype in brightness_contrast

import numpy as np
import matplotlib.pyplot as plt
import cv2
# from google.colab.patches import cv2.imshow
'win',

def hue_saturation(img_rgb, alpha = 1, beta = 1):
  img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
  hue = img_hsv[:,:,0]
  saturation = img_hsv[:,:,1]
  hue = np.clip(hue * alpha,0,179)
  saturation = np.clip(saturation * beta,0,255)
  img_hsv[:,:,0] = hue
  img_hsv[:,:,1] = saturation
  img_transformed = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
  return img_transformed

def brightness_contrast(img, alpha = 1.0, beta = 0):
  img_contrast = img * (alpha)
  img_bright = img_contrast + (beta)
  img_bright = np.clip(img_bright, 0 , 255)
  # img_bright = img_bright.astype(np.unit8)
  return img_bright

def grayscale(img):
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img_gray

def vignette(img,r,g,b,a):
  color = img.copy()
  color[:,:,0] = b
  color[:,:,1] = g
  color[:,:,2] = r
  res = cv2.addWeighted(img,1-a,color,a,0)
  return res

def replace_color(img,hl=0,sl=0,vl=0,hu=0,su=0,vu=0,nred=0,ngreen=0,nblue=0):
  rows,cols = img.shape[:2]
  i_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower = np.array([hl,sl,hu])
  upper = np.array([hu,su,vu])
  color = cv2.inRange(i_hsv,lower,upper)
  img[color>0]=(nblue,ngreen,nred)
  return img


def Amaro(img, hue = 1.1, saturation = 1.5, contrast = 0.9, brightness = 10):
  img = hue_saturation(img, hue, saturation)
  img = brightness_contrast(img, contrast, brightness)
  return img

def Nashville(img, hue = 1, saturation = 1.5, contrast = 1.2, brightness = 10):
  img = hue_saturation(img, hue, saturation)
  img = brightness_contrast(img, contrast, brightness)
  img = replace_color(np.float32(img),0,0,0,0,0,30,34,43,109)
  img = replace_color(np.float32(img),0,0,200,0,0,255,247,218,174)
  #img = vignette(img,247,218,174,0.2)
  return img
                        

img = cv2.imread('doge.jpg')
cv2.imshow('win',img)

# # plt.gcf().set_size_inches(25,25)
# # plt.subplot(131),plt.imshow(img),plt.title('Original')
# # plt.xticks([]), plt.yticks([])

img_amaro = Amaro(img)
# # img_amaro = Amaro(cv2.cvtColor(img,cv2.COLOR_BGR2RGB ) )


# # plt.subplot(132),plt.imshow(img_amaro),plt.title('Amaro')
# # plt.xticks([]), plt.yticks([])

cv2.imshow('win',img_amaro)
# # plt.show(img_amaro)

# # plt.subplot(133),plt.imshow(img),plt.title('Averaging - 5x5')
# # plt.xticks([]), plt.yticks([])

img_nashville = Nashville(img)
cv2.imshow('win',img_nashville)


# plt.show()