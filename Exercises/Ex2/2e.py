import cv2
import numpy as np

img = cv2.imread('../resources/img.jpg')

b, g, r = cv2.split(img)

cv2.namedWindow("blue")
cv2.namedWindow("green")
cv2.namedWindow("red")
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

value = 40
b += value
newimg = cv2.merge((b, g, r))

cv2.namedWindow("window")
cv2.imshow("window", newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

