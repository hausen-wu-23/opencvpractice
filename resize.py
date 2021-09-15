import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parser.parse_args())

img =  cv2.imread(args['image'])
cv2.imshow('original image', img)

newW = 150.0
ratio = newW / img.shape[1]
dimension = (int(newW), int(img.shape[0] * ratio))

resized =cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("resized width: %i" % newW, resized)

newH = 50.0
ratio = newH / img.shape[0]
dimension = (int(img.shape[1] * ratio), int(newH))

resized =cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("resized height: %i" % newH, resized)

resized = imutils.resize(img, height=100)
cv2.imshow('Resized by function',resized)
cv2.waitKey(0)