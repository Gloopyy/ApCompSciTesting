import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Crops image
#Giving numpy array slices
#From (240,30) to (335,120)
#Argument format - image[y1:y2 , x1:x2]
cropped = image[30:120 , 240:335]
cv2.imshow("Banana Cropped", cropped)
cv2.waitKey(0)