import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (9, 9), 0)
# blurred = cv2.bilateralFilter(img, 9, 41,41)

cv2.imshow('original', np.vstack([img, blurred]))

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
print(T)
cv2.imshow('thresh binary', thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
print(T)
cv2.imshow('thresh binary inv', threshInv)

cv2.imshow('coins', cv2.bitwise_and(img, img, mask=threshInv))

cv2.waitKey(0)