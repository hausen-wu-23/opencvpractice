import numpy as np
import argparse
import cv2
import mahotas as mh

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
# blurred = cv2.bilateralFilter(img, 9, 41,41)

cv2.imshow('original', np.vstack([img, blurred]))

T= mh.thresholding.otsu(blurred)
print("otsu: %d" % T)

threshOtsu = img.copy()
threshOtsu[threshOtsu>T] = 255
threshOtsu[threshOtsu<255] = 0
threshOtsu = cv2.bitwise_not(threshOtsu)

T= mh.thresholding.rc(blurred)
print("riddler calvard: %d" % T)

thresh = img.copy()
thresh[thresh>T] = 255
thresh[thresh<255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('otsu + riddler', np.hstack([threshOtsu, thresh]))

cv2.waitKey(0)