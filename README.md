# Counting-dices
<p>This is a program to count the dots on a dice.</p>

# How does it work
## Import
<p>This program uses two libraries. The opencv and numpy library.</p>

```py
import cv2
import numpy as np
```

# Import image
<p>Next you need to import the image. On the place where is written "link to image" you need to place the path to the image.<br>
Also we have to convert the image from BGR to gray.</p>

```py
img = cv2.imread("link to image")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```