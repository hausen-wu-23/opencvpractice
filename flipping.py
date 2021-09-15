import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='Path to image')

args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

flipped = cv2.flip(img, 0)
cv2.imshow("vertically", flipped)

cv2.waitKey(0)