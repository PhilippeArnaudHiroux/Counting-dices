#Sources
#https://www.geeksforgeeks.org/python-opencv-cv2-blur-method/
#https://thepythoncode.com/article/canny-edge-detection-opencv-python?utm_content=cmp-true
#https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

#Imports
import cv2
import numpy as np

#Read the image and convert it to a gray image
img = cv2.imread("link to image")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply a Gaussian Blur filter to the image and display the blurred image
kernel_size = (15, 15)
blur = cv2.GaussianBlur(grayImage, kernel_size, 0)
cv2.imshow("Gausian", blur)

#Detect and display the edges
edges = cv2.Canny(blur, threshold1=30, threshold2=100)
cv2.imshow("edges", edges)

#Detect the circles on the edges image
detected_circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,  param2 = 21, minRadius = 1, maxRadius = 50)

#Draw the circles that have been detected
if detected_circles is not None:

    #Convert the circle parameters to integers
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        #Draw the circle in green on the original image
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        #Draw the center of the circle in red on the original image
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        #Display the original image with the circles on it
        cv2.imshow("Detected Circle", img)

#Print out the number of circles (detected circles is an array with 3 values for each circle. That is why detected_circles is divided by 3)
print(detected_circles.size/3)

#Wait for the user to press a key
cv2.waitKey(0)