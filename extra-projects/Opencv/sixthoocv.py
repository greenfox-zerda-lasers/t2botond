import cv2
import numpy as np
img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.jpg')

#px = img[300, 500]
#print(px)

img.item(10, 10, 2)

img.itemset((10, 10, 2), 100)
img.item(10, 10, 2)

print(img.shape)
print(img.size)
print(img.dtype)

scrap = img[ 150:350, 500:800]
img[350:550, 800:1100] = scrap

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
img[:,:,2] = 0

cv2.imshow('pic', img)
cv2.waitKey(0)
