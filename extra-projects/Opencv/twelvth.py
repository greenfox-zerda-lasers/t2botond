import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.JPG')
res = cv2.resize(img, None, fx=1, fy=1, interpolation =cv2.INTER_CUBIC)
rows, cols, ch = res.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0, 0],[300, 0],[0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(res), plt.title('Input')
plt.subplot(121), plt.imshow(dst), plt.title('Output')
plt.show()
