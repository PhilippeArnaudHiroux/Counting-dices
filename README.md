# Counting-dices
<p>This is a program to count the dots on a dice.</p>

# How does it work
## Import
<p>This program uses two libraries. The opencv and numpy library.</p>

```py
import cv2
import numpy as np
```

## Import image
<p>Next you need to import the image. On the place where is written "link to image" you need to place the path to the image.<br>
Also we have to convert the image from BGR to gray.</p>

```py
img = cv2.imread("link to image")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

## Image blur
<p>To reduce the noise on the image, the image need to be blurred. For this we use a GaussianBlur filter.</p>

```py
kernel_size = (15, 15)
blur = cv2.GaussianBlur(grayImage, kernel_size, 0)
cv2.imshow("Gausian", blur)
```

## Edge detection
<p>To make it easier to detect circles, we use the cv2.canny function to detect the edges</p>

```py
edges = cv2.Canny(blur, threshold1=30, threshold2=100)
cv2.imshow("edges", edges)
```

## Circle detection
<p>With the cv2.HoughCircles function its possible to find circles. Every circle will have three parameters: a x coordinate, a y coordinate and a radius.<br>
The cv2.circle function is used twice. The first time it will draw the circle on the original image, and the second time it puts a dot in the middle of the circle.</p>

```py
detected_circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,  param2 = 21, minRadius = 1, maxRadius = 50)

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        cv2.imshow("Detected Circle", img)
```

## Print out size
<p>At the end we print out the size by dividing the detected_circles array by three</p>

```py
print(detected_circles.size/3)
```

# Sources
