import argparse
import cv2

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--image', required=True, help='path to image')

args = vars(parse.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

print(type(image))

(b, g, r) = image[0,0]
print("pixel at (0, 0)'s rgb value is %i %i %i" % (r, g, b))

image[0,0] = (0, 0 ,0)

(b, g, r) = image[0,0]
print("pixel at (0, 0)'s rgb value is %i %i %i" % (r, g, b))

top_left = image[:100,:100]
cv2.imshow("top left", top_left)

image[:50,:50] = (0,250,0)

cv2.imshow("updated", image)
cv2.waitKey(0)
