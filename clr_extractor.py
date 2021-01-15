import cv2
import numpy as np

img = cv2.imread("Images/185.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#lower_red = np.array([0, 100, 0]) 
#upper_red = np.array([5, 255, 255])

lower_white = np.array([23, 16, 88]) 
upper_white = np.array([59, 55, 146])

#Define threshold color range to filter
mask = cv2.inRange(hsv, lower_white, upper_white)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('MASKING',mask)
cv2.imshow('ORIGINAL_IMAGE', img)
cv2.imshow('ONLY_COLORED', res)

cv2.waitKey(0)
cv2.destroyAllWindows()