#import libraries
#print statement works in python 2.7 and 3
from __future__ import print_function
#Argparse used to parse cmd arguments
import argparse
#CV2 used to process images
import cv2

#Setup argparse
ap = argparse.ArgumentParser()
#Adds --image argument to command
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
#Parse arguments, store in dictionary
args = vars(ap.parse_args())

#Following lines show image
image = cv2.imread(args["image"])
#Name of window, then name of image variable (from previous line)
cv2.imshow("Original", image)


#Get pixel at (0, 0), store BGR values
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#Make top left pixel red
image[0, 0] = (0, 0, 255)
#Prepare for printing
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#Store top left 100x100 pixels as corner
corner = image[0:100, 0:100]
#Show
cv2.imshow("Corner", corner)

#Make corner green
image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
#Don't show until key is pressed, 0 means any key
cv2.waitKey(0)

#Run with:
#python getting_and_setting.py --image ../images/banana.png
