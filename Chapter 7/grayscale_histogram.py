from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

#Compute histogram
#Grayscale is one channel, so 0 is channels
#No mask
#256 bins
#Bin values from 0-256
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

#Create graph
plt.figure()
#Set title
plt.title("Grayscale Histogram")
#Title x-axis
plt.xlabel("Bins")
#Title y-axis
plt.ylabel("# of Pixels")
#Plots histogram
plt.plot(hist)
#Set x limit
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)