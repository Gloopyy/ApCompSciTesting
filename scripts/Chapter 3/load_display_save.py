from __future__ import print_function
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to Image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Picture", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
