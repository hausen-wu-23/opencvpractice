import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
# blurred = cv2.bilateralFilter(img, 9, 41,41)

cv2.imshow('original', np.vstack([img, blurred]))

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow('mean', thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow('gaussian', thresh)

cv2.waitKey(0)