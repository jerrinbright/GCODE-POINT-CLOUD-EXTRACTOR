import cv2
import numpy as np


img = cv2.imread("Images/185.jpg")

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

#converting to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# get info from track bar and appy to result
h = cv2.getTrackbarPos('h','result')
s = cv2.getTrackbarPos('s','result')
v = cv2.getTrackbarPos('v','result')

# Normal masking algorithm
lower_blue = np.array([h,s,v])
upper_blue = np.array([180,255,255])

mask = cv2.inRange(hsv,lower_blue, upper_blue)

result = cv2.bitwise_and(img,img,mask = mask)

cv2.imshow('result',result)

k = cv2.waitKey(0) 
while 1:    
  if k == 27:
    break

img.release()
cv2.destroyAllWindows()