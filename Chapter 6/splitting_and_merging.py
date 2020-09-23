import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#Split image into channels
(B, G, R) = cv2.split(image)

cv2.imshow("Red ", R)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.waitKey(0)

#Merge channels
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
#Close all windows
cv2.destroyAllWindows()

#Make numpy array of zeros with same dimensions as image
zeros = np.zeros(image.shape[:2], dtype = "uint8")
#Set B & G channels to zeros
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
#Set B & R channels to zeros
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
#Set R & G channels to zeros
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)