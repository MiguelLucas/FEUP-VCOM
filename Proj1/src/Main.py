# import cv2
import numpy as np
import Utils
from Camera import *

img = captureCamera()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("window")
cv2.imshow("window", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()



