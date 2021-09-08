import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (203, 206, 134)
cv2.line(canvas, (0, 0), (300, 300), green, 3)

red = (77, 30, 232)
cv2.line(canvas, (300, 0), (0, 300), red, 3)

cv2.rectangle(canvas, (10, 10), (50, 50), green, -1)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (240, 240, 240)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white, 2)

for i in range(0, 10):
    radius = np.random.randint(5, high=200)
    colour = np.random.randint(0, high=256, size=3).tolist()
    centre = np.random.randint(0, high=300, size=2)

    print(type(centre))

    cv2.circle(canvas, tuple(centre), radius, colour, -1)



cv2.imshow("canvas", canvas)

cv2.waitKey(0)