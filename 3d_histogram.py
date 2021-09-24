from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required = True)
parser.add_argument('-s', '--size', required = False, default=5000)
parser.add_argument('-b', '--bins', required = False, default=8)
args = vars(parser.parse_args())

img = cv2.imread(args['image'])
size = float(args['size'])
bins = int(args['bins'])

cv2.imshow('original', img)

hist = cv2.calcHist([img], [0,1,2], None, [bins, bins, bins], [0,256,0,256,0,256])

print('3d histogram shape: %s with %d values' % (hist.shape, hist.flatten().shape[0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ratio = size/np.max(hist)

for (x, plane) in enumerate(hist):
    for (y, row) in enumerate(plane):
        for (z, col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio * hist[x][y][z]
                rgb = (z/(bins-1), y/(bins-1), x/(bins-1))
                ax.scatter(x,y,z,s=siz,facecolors=rgb)

plt.show()