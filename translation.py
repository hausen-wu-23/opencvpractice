import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parser.parse_args())

img =  cv2.imread(args['image'])
cv2.imshow('original image', img)

# M = np.float32([[1, 0, -25], [0, 1, -50]])
# shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

shifted = imutils.translate(img, 0, -100)
cv2.imshow('shifted', shifted)

cv2.waitKey(0)