import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')

# to hide tick values on X and Y axis
# plt.xticks([]), plt.yticks([])
plt.show()
