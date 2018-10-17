import cv2
import numpy as np

height = 100
width = 200

img = np.zeros((height, width), np.uint8)
img.fill(100)

y = 0
for x in range(0, height):
    if y < width-2:
        y += 2
    img[x, y] = 255
    img[height - x - 1, y] = 255

cv2.namedWindow("window1")
cv2.imshow("window1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
