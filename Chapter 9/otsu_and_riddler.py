from __future__ import print_function
import numpy as np
import argparse
import mahotas
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

#Calculate optimal T value with otsu
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

#Copy image
thresh = image.copy()
#Make values above T white
thresh[thresh > T] = 255
#Make values below T black
thresh[thresh < 255] = 0
#Invert image
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

#Calculate optimal T value with Riddler-Calvard
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
#Copy image
thresh = image.copy()
#Make values above T white
thresh[thresh > T] = 255
#Make values below T black
thresh[thresh < 255] = 0
#Invert image
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)