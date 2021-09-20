from matplotlib import pyplot as plt
import cv2
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', img)

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title('grascale')
plt.xlabel('bin')
plt.ylabel('# of pixels')
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
