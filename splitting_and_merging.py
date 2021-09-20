import cv2
import numpy as np
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
(b, g, r) = cv2.split(img)

cv2.imshow('r', r)
cv2.imshow('g', g)
cv2.imshow('b', b)
cv2.waitKey(0)

merge = cv2.merge([b, g, r])
cv2.imshow('merge', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('r', cv2.merge([zeros, zeros, r]))
cv2.imshow('g', cv2.merge([zeros, g, zeros]))
cv2.imshow('b', cv2.merge([b, zeros, zeros]))
cv2.waitKey(0)