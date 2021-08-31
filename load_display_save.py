from __future__ import print_function
import argparse

import cv2

parse = argparse.ArgumentParser()
parse.add_argument("-i", "--image", required=True, help="Path to the Image")

args = vars(parse.parse_args())

print(args)

img = cv2.imread(args["image"])


print("width: %i pixels" % img.shape[1])
print("height: %i pixels" % img.shape[0])
print("channels: %i" % img.shape[2])

cv2.imshow("TRex", img)

cv2.waitKey(0)
