import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Photos/sekiro.jpg')

color = {'b', 'g', 'r'}  # 在不同的通道上进行统计

for i, col in enumerate(color):
    histr = cv2.clacHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()