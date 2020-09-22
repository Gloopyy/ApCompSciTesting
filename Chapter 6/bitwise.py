import numpy as np
import cv2

#Initialize rectanglular image
#300x300 numpy array
rectangle = np.zeros((300, 300), dtype = "uint8")
#Draw 250x250 white rectangle at center
#Arguments - image, start point, end point, color, thickness
#From (25, 25) to (275, 275)
#255 for white
#-1 to fill in
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

#Initialize rectangular image
#300x300 numpy array
circle = np.zeros((300, 300), dtype = "uint8")
#Draw circle with radius of 150
#Arguments - image, center coordinates, radius, color, thickness
#Center at (150, 150), center of image
#Radius of 150
#255 for white
#-1 to fill in
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

#Compare 2 pixels to use bitwise functions
#Modifies images
#Turns on pixels that are true, turns off pixels that are false

#AND - true when both pixels > 0
#Removes areas that don't overlap in images
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

#OR - true when at least one pixel > 0
#Combines images
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

#XOR - true when only one pixel > 0
#Removes overlapping areas
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

#NOT - inverts "on" and "off" pixels in image
#Inverts colors
bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)