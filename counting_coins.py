import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True,
help = "path to the image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("image", blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("edges", edged)

cv2.waitKey(0)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('%d coins' % len(cnts))

coins = img.copy()
cv2.drawContours(coins, cnts, -1, (0, 0, 255), 2)
cv2.imshow('coins', coins)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    print('coin #%d' % i)
    coin = img[y:y+h, x:x+w]
    cv2.imshow("coin", coin)

    mask = np.zeros(img.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow('coin', cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)