import numpy as np
import cv2

# Read in the image
img = cv2.imread("faces.jpeg",1)

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_eye.xml"

# Load the xml file as our cascade classifier
eye_cascade = cv2.CascadeClassifier(path)

# List of eyes
eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.02, minNeighbors = 20, minSize = (10, 10))
print(eyes)

# Draw circles around detected eyes

for (x,y,w,h) in eyes:
    # Compute coordinates of centre of the circle
    xc = (x + (x + w))/2
    yc = (y + (y + h))/2
    radius = w/2
    cv2.circle(img, (int(xc), int(yc)), int(radius), (0, 255, 0), 2)
  
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()