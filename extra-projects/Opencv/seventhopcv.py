import cv2
import numpy as np
e1 = cv2.getTickCount()
img1 = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/slice_2_1.png')
img2 = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/slice_0_0.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
e2 = cv2.getTickCount()
t = (e2-e1) / cv2.getTickFrequency()
print(t)
cv2.waitKey(0)
cv2.destroyAllWindows()
