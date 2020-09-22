from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#CV2 ARITHMETIC
#Define 2 numpy arrays
#Array one: One element with value of 200
#Array two: One element with value of 100
#Add values together
#Output is 300, but cv2.add caps it at 255
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
#Similar to above, but with subtracting
#Output is -50, but cv2.subtract caps it at 0
print("max of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

#NUMPY ARITHMETIC
#Define 2 numpy arrays
#Array one: One element with value of 200
#Array two: One element with value of 100
#Add values together
#Output is 300, but numpy wraps around so output is 44
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
#Similar to above, but with subtracting
#Output is -50, but numpy wraps around so output is 206
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

#Define numpy array of ones, same size as image
#Uses 8 bit unsigned integers as data type
#Multiply by 100 to make it an array of 100s
#Add matrix of 100s to image, increasing intensity
#Caps at 255 by cv2.add
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

#Define numpy array of ones, same size as image
#Uses 8 bit unsigned integers as data type
#Multiply by 50 to make it an array of 50s
#Subtract matrix of 50s from image, deincreasing intensity
#Caps at 0 by cv2.subtract
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)