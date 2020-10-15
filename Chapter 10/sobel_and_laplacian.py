import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

#Compute gradient magnitude
#Arguments - image, data type (64-bit float here)
#Not using a floating point data type will miss some edges
lap = cv2.Laplacian(image, cv2.CV_64F)
#Take absolute value of gradient image and convert it to uint8
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

#Compute gradient magnitude with sobel across axes
#Arguments - image, data type, x, y
#1 for x and 0 for y to find vertical edge-like areas
#0 for x and 1 for y to find vertical edge-like areas
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

#Take absolute value and convert to uint8
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#Combine images
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.waitKey(0)
cv2.imshow("Sobel Y", sobelY)
cv2.waitKey(0)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
