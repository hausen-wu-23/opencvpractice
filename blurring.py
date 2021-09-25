import numpy as np
import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

blurred = np.hstack([
        cv2.blur(img, (3, 3)), 
        cv2.blur(img, (5, 5)), 
        cv2.blur(img, (21, 21))
    ])

blurred = np.vstack([
    blurred, 
    np.hstack([
        cv2.GaussianBlur(img, (3, 3), 0), 
        cv2.GaussianBlur(img, (5, 5), 0), 
        cv2.GaussianBlur(img, (21, 21), 0)
    ])
])

blurred = np.vstack([
    blurred,
    np.hstack([
        cv2.medianBlur(img, 3),
        cv2.medianBlur(img, 5),
        cv2.medianBlur(img, 21),
    ])
])

blurred = np.vstack([
    blurred,
    np.hstack([
        cv2.bilateralFilter(img, 5, 21, 21),
        cv2.bilateralFilter(img, 7, 31, 31),
        cv2.bilateralFilter(img, 9, 41, 41),
    ])
])



cv2.imshow('blurred', blurred)



cv2.waitKey(0)
