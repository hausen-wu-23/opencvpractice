import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='Path to image')

args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

mask = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
cv2.imshow("mask", mask)

masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("masked img", masked)
cv2.waitKey(0)

mask = np.zeros(img.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("circlee", mask)
cv2.imshow("circle masked img", masked)
cv2.waitKey(0)