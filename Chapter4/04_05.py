import numpy as np
import cv2

# Face detection using Haar cascade method

# Read in the image
img = cv2.imread("faces.jpeg",1)

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"

# Load the xml file as our cascade classifier
face_cascade = cv2.CascadeClassifier(path)

# List of faces
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.10, minNeighbors = 5, minSize = (40,40))
print(faces)

# Draw rectangles around detected faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()