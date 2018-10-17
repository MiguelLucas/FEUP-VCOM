import cv2
import numpy as np

img = cv2.imread('../resources/img.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("window1")
cv2.imshow("window1", gray_img)
cv2.imwrite('../resources/image_2c.png', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


