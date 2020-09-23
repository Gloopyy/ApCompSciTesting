import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Make numpy array of zeros
#Same dimensions as image
mask = np.zeros(image.shape[:2], dtype = "uint8")
#Find center
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
#Draw rectangle in center 150x150
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

#Apply AND
#First two parameters are the image (bitwise needs 2 images)
#Bitwise only examines pixels in the mask
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

#Make numpy array of zeros
mask = np.zeros(image.shape[:2], dtype = "uint8")
#Draw circle in center
cv2.circle(mask, (cX, cY), 100, 255, -1)
#Apply mask
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)