import cv2
import numpy as np

img = cv2.imread('../resources/img.jpg')
grayscale = False

size = img.size

if len(img.shape) < 3:
    grayscale = True

n_salt = int(round(size * 0.10))

if grayscale is True:
    for x in range(0, len(img)):
        print x

#TODO

print n_salt

