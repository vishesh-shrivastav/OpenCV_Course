import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

for c in contours:
    cv2.drawContours(objects, [c], -1, color, -1)
    # Get areas and perimeters of contours
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    
    # Get centroid
    m = cv2.moments(c)
    cx = int(m['m10']/m['m00'])
    cy = int(m['m01']/m['m00'])
    
    cv2.circle(objects, (cx, cy), 4, (0,0,255), -1)
    
    print("Area: {}, Perimeter{}".format(area, perimeter))
    
cv2.imshow("Contours", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
