import cv2
import numpy as np

img = cv2.imread("Images/185.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   
lower_red = np.array([81, 31, 48])
upper_red = np.array([180,255,255])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
    
k = cv2.waitKey(5) & 0xFF
while 1:
  if k == 27:
    break

cv2.destroyAllWindows()
cap.release()