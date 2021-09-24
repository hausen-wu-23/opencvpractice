from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256],[0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])
    
    plt.show()

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')
args = vars(parse.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('original', img)
plot_histogram(img, 'original')

mask = np.zeros(img.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15,15), (130,100), 255, -1)
cv2.imshow('mask', mask)

masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('masked img', masked)

plot_histogram(img, 'masked', mask)

cv2.waitKey(0)