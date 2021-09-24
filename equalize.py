from matplotlib import pyplot as plt
import cv2
import argparse
import numpy as np

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
original = cv2.calcHist([img], [0], None, [255], [0, 256])

plt.figure()
plt.title('original')
plt.xlabel('bin')
plt.ylabel('# of pixels')
plt.plot(original)
plt.xlim([0, 256])
plt.show()

eq = cv2.equalizeHist(img)
eqed = cv2.calcHist([eq], [0], None, [255], [0, 256])

plt.figure()
plt.title('equalised')
plt.xlabel('bin')
plt.ylabel('# of pixels')
plt.plot(eqed)
plt.xlim([0, 256])
plt.show()

cv2.imshow('histogram equalise', np.hstack([img, eq]))



cv2.waitKey(0)