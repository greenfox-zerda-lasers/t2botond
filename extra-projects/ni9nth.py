import cv2
import numpy as np
img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.JPG')
res = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation =cv2.INTER_CUBIC)

cv2.imshow('img',res)
cv2.waitKey(0)
