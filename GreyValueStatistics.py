import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Photos/sekiro.jpg', 1)

plt.hist(img.reshape([-1]), 256, [0, 256])
plt.show()