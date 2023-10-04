#Philippe-Arnaud Hiroux
#Opdracht 2e zit image processing

#Bronnen
#https://www.geeksforgeeks.org/python-opencv-cv2-blur-method/
#https://thepythoncode.com/article/canny-edge-detection-opencv-python?utm_content=cmp-true
#https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

#Imports
import cv2
import numpy as np

#Lees de afbeelding in en zet het om naar een grijze afbeelding
img = cv2.imread("link to image")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Pas een GausianBlur filter toe op de afbeedling en geef de geblurde afbeelding weer
kernel_size = (15, 15)
blur = cv2.GaussianBlur(grayImage, kernel_size, 0)
cv2.imshow("Gausian", blur)

#Detecteer de edges en geef deze weer
edges = cv2.Canny(blur, threshold1=30, threshold2=100)
cv2.imshow("edges", edges)

#Detecteer de cirkels op de edges afbeelding
detected_circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,  param2 = 21, minRadius = 1, maxRadius = 50)

#Teken de cirkels die gedetecteerd zijn
if detected_circles is not None:

    #Converteer de cirkel parameters naar integers
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        #Teken de cirkel in het groen op de orginele afbeelding
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        #Teken het middel punt van de cirkel in het rood op de orginele afbeelding
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        #Geef de orginele afbeelding weer met de cirkels erop
        cv2.imshow("Detected Circle", img)

#Print uit het aantal cirkels (detected_circles is een array met voor elke cirkel 3 waardes. Daarom wordt detected_circles gedeeld door 3)
print(detected_circles.size/3)

#Wacht tot de gebruiker een toets in duwt
cv2.waitKey(0)