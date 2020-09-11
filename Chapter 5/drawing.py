import numpy as np
import cv2

#Make numpy array with 300 rows and columns (300x300 pixels), set 3 channels (RGB)
#zeros sets initial value to zero for each pixel
#uint8 is an 8-bit integer, and is used because image is RGB
canvas = np.zeros((300, 300, 3), dtype= "uint8")

#LINES

#Define tuple for BGR green
green = (0, 255, 0)
#Draw line from top left to bottom right in green
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#Define tuple for BGR red
red = (0, 0, 255)
#Draw line from top right to bottom left in red with 3 pixels of thickness
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#RECTANGLES

#Draw rectangle from two points in green
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#Draw rectangle from two points in red with thickness of 5
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
#Draw rectangle from two points in blue that is filled in
cv2.rectangle(canvas, (200,50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#CIRCLES

#Erase everything on canvas
canvas = np.zeros((300, 300, 3), dtype= "uint8")
#Make variables centerX and centerY, the x and y coords of the circle's center
#To find center, width and height are divided by 2
#Height = canvas.shape[0]
#Width = canvas.shape[1]
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

#Loop for multiple radius values between 0 & 150 in increments of 25
#for is exclusive, so 175 isn't included
for r in range(0, 175, 25):
    #Draws circle from center of image with a radius of r in white
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#Loop 25 times
for i in range(0, 25):
    #Random radius between 5 and 199
    radius = np.random.randint(5, high = 200)
    #Random color, generates 3 numbers between 0 and 255
    #size=(3,) returns 3 numbers
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    #Random point on canvas, generates two values (x and y) between 0 and 299
    pt = np.random.randint(0, high = 300, size = (2,))

    #Draw circle from random values
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
