import cv2
import numpy as np

img = cv2.imread('../resources/img.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)

cv2.namedWindow("h")
cv2.namedWindow("s")
cv2.namedWindow("v")
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey(0)
cv2.destroyAllWindows()

value = 1
s += value
newimg = cv2.merge((h, s, v))

cv2.namedWindow("window")
cv2.imshow("window", newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
