import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parser.parse_args())

img =  cv2.imread(args['image'])
cv2.imshow('original image', img)
# (h, w) = img.shape[:2]
# center = (w//2, h//2)

# M = cv2.getRotationMatrix2D(center, 45, 0.5)
# rotate = cv2.warpAffine(img, M, (w,h))
# cv2.imshow("rotated image", rotate)

rotated = imutils.rotate(img, 45, scale=0.5)
cv2.imshow("rotate", rotated)

cv2.waitKey(0)