import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0 , 0) # place window at top left

print(color.shape)

height, width, channel = color.shape

b,g,r = cv2.split(color) # Split channel into components

rgb_split = np.empty([height, width * 3, 3], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b,b,b]) # Place blue channel on left side of image
rgb_split[:, width:width*2] = cv2.merge([g,g,g]) # Place green channel at center of image
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r]) # Place red channel on right side of image

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

# Hue saturation
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis = 1)

cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()