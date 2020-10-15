import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#Convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Apply gaussian blur
#Removes some hard edges
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)
cv2.waitKey(0)

#Compute thresholded image
#Args - Image, T value, value to give to pixels above T, thresholding method
#THRESH_BINARY sets values higher than T to max value (third agrument)
#Returns T and image
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

#THRESH_BINARY_INV is inverse of previous
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.waitKey(0)

#Mask image
#Arguments - original image, original image, image to use as mask (give inverted threshold image)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)