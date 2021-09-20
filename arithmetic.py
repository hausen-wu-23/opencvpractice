import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='Path to img')

args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))


M = np.ones(img.shape, dtype = "uint8") * 100
added = cv2.add(img, M)
cv2.imshow("Added", added)

M = np.ones(img.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(img, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)