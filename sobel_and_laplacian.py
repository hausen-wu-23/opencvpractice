import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('lapacian', lap)
cv2.waitKey(0)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow('sobelx', sobelX)
cv2.imshow('sobely', sobelY)
cv2.imshow('sobelc', sobelCombined)

cv2.waitKey(0)