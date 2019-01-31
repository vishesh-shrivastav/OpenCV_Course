import cv2

img = cv2.imread("opencv-logo.png", 1) # Read default colors and channels by passing in 1

#img.shape
#(739, 600, 3)

# Create window to view image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# View image in window
cv2.imshow("Image", img)
cv2.waitKey(0) # Make the image window wait till the user interacts with it

# Write image to disk
cv2.imwrite("output.jpg", img)
