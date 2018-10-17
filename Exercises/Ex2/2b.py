import cv2
import numpy as np

height = 50
width = 200
ratio = width / height

img = np.zeros((height, width, 3), np.uint8)
img.fill(100)

y = 0
for x in range(0, height):
    if y < width-ratio:
        y += ratio
    img[x, y] = [255, 0, 0]
    img[height - x - 1, y] = [0, 0, 255]

cv2.namedWindow("window1")
cv2.imshow("window1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
