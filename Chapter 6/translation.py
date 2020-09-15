#Import packages
import numpy as np
import argparse
#Imutils creates methods
import imutils
import cv2

#Setup arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

#Loads and displays image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Define translation matrix (M)
#Says how many pixels in a direction image should move
#Is a floating point array, expected for OpenCV
#25 pixels to the right (positive to the right, negative to the left)
#50 pixels down (positive down, negative up)
M = np.float32([[1, 0, 25], [0, 1, 50]])
#warpAffine function used to translate image
#Arguments - Image to shift, matrix, dimensions of image
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#Show translated image
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

#50 pixels to the left
#90 pixels up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

#Use imultils function, created in imutils.py script
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
