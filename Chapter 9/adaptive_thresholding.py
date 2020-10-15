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

#Apply adaptive thresholding
#Arguments - image, max value, method for computing threshold, thresholding method, surrounding pixel size (11x11), C (subtracted from mean, used to fine tune thresholding)
#ADAPTIVE_THRESH_MESH_C computes average of surrounding pixels and uses it as T value
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 7)
cv2.imshow("Mean Thresh", thresh)
cv2.waitKey(0)

#ADAPTIVE_THRESH_GAUSSIAN_C uses weighted mean
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Mean Thresh", thresh)
cv2.waitKey(0)
