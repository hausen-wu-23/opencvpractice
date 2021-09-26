import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('blurred', img)

canny = cv2.Canny(img, 30, 150)
cv2.imshow('canny', canny)
cv2.waitKey(0)