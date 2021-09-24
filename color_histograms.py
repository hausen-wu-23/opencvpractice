from matplotlib import pyplot as plt
import cv2
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)

channels = cv2.split(img)
colors = ('b', 'g', 'r')
plt.figure()
plt.xlabel('bins')
plt.ylabel('# of pix')

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title('2d color histogram for g and b')
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title('2d color histogram for g and r')
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title('2d color histogram for b and r')
plt.colorbar(p)

print('2d histogram shape: %s, with %i values' % (hist.shape, hist.flatten().shape[0]))

hist = cv2.calcHist([img], [0, 1, 2], None, [8,8,8], [0,256,0,256,0,256])
print('3d, histogram shape: %s, with %i values' % (hist.shape, hist.flatten().shape[0]))


plt.show()

cv2.waitKey(0)