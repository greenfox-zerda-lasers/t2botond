import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.JPG')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50],[20, 200]])
pts2 = np.float32([[10, 100],[200, 50],[100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(121),plt.imshow(dst),plt.title('Output')
plt.show()
