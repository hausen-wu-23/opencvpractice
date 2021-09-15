import numpy as np
import cv2

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return(shifted)

def rotate(img, angle, ctr=None, scale=1.0):
    (h, w) = img.shape[:2]
    if ctr is None:
        ctr = (w//2, h//2)

    M = cv2.getRotationMatrix2D(ctr, angle, scale)
    rotated = cv2.warpAffine(img, M, (w,h))

    return rotated

def resize(img, width=None, height=None, alg=cv2.INTER_AREA):
    (h, w) = img.shape[:2]

    if width is None and height is None:
        raise Exception('Both width and height are empty')

    if width is None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    
    elif height is None:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    else:
        dimension = (width, height)

    resized = cv2.resize(img, dimension, interpolation=alg)
    return resized