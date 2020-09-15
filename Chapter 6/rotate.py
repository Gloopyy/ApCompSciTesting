import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Get width and height of image
(h, w) = image.shape[:2]
#Divides width and height by 2 to find center
#// is used to ensure output is a whole number
center = (w // 2, h // 2)

#Define rotation matrix
#Rotate 45 degrees
#Arguments - point of rotation, degrees to rotate, image scale
M = cv2.getRotationMatrix2D(center, 45, 1.0)
#Apply rotation
#Arguments - image, matrix, output dimensions
rotated = cv2.warpAffine(image, M, (w, h))
#Show image
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

#Define rotation matrix
#Rotate -90 degrees
M = cv2.getRotationMatrix2D(center, -90, 1.0)
#Apply rotation
rotated = cv2.warpAffine(image, M, (w, h))
#Show image
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

#Use imutils rotate function
rotated = imutils.rotate(image, 180)
#Show image
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
