import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg",1)

# Edge detection algorithms look at the rate at which color changes to determine edges

# Approach 1 - Thresholding
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV) # extract all pixels with hue value of 25 or less

cv2.imshow("Thresh", thresh)

# Canny edge detection
edges = cv2.Canny(img, 100, 70)

cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()