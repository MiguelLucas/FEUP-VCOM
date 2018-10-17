import numpy as np
import cv2

img = cv2.imread('resources/img.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('resources/image_1b.png', img)
cv2.destroyAllWindows()
