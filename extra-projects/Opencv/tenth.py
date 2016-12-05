import cv2
import numpy as np
img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.JPG',0)
res = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation =cv2.INTER_CUBIC)
rows,cols = res.shape

#M = np.float32([[1,0,100],[0,1,50]])
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90,1)
dst = cv2.warpAffine(res, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
