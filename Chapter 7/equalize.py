import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Convert image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Equalize histogram
eq = cv2.equalizeHist(image)

#Show grayscale and equalized image side-by-side
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)