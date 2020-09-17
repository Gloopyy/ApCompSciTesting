import numpy as np
import argparse
import imutils
import cv2

ap =argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Get aspect ratio
#Make new image width 150 pixels
#Set ratio 'r' as width divided by previous width
r = 150.0 / image.shape[1]
#Find new dimensions
#Arguments - width, height
#New height is found by multplying old height by ratio
dim = (150, int(image.shape[0] * r))

#Resize image
#Arguments - image, dimensions, interpolation method
#Interpolation method is algorithm used to resize
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

#Set ratio 'r' as height divided by previous height
r = 50.0 / image.shape[0]
#New width is found by multplying old width by ratio
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized (width) via Function", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height = 50)
cv2.imshow("Resized (height) via Function", resized)
cv2.waitKey(0)
