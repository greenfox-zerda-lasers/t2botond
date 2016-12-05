import numpy as np
import cv2
from matplotlib import pyplot as plt
import tkinter

img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
#img = cv2.imread('D:/greenfox/Greenfox/t2botond/extra-projects/Opencv/rodacar.jpg', 0)
#cv2.imshow("roda", img)
#k = cv2.waitKey(0) & 0xFF
#if k == 27:
#    cv2.destroyAllWindows()
#elif k == ord('s'):
#    cv2.imwrite('rodacaringrey.png', img)
#    cv2.destroyAllWindows()
