import cv2
import random
import numpy as np

img = np.zeros((800, 800, 3), np.uint8)

lx1 = random.randint(0, 700)
ly1 = random.randint(0, 700)
lx2 = random.randint(0, 700)
ly2 = random.randint(0, 700)

rx = random.randint(0, 200)
ry = random.randint(0, 200)
rw = random.randint(300, 500)
rh = random.randint(300, 500)

ex1 = random.randint(0, 600)
ey1 = random.randint(0, 600)
exl = random.randint(50, 200)
eyl = random.randint(30, 100)

cx = random.randint(0, 600)
cy = random.randint(0, 600)
cr = random.randint(70, 200)

cv2.line(img, (lx1, ly1), (lx2, ly2), (232, 255, 0), 5)

cv2.rectangle(img, (rx, ry), (rx + rw, ry + rh), (0, 255, 0), 3)

cv2.ellipse(img, (ex1, ey1), (exl, eyl), 0, 0, 360, (214, 51, 192), -1)

cv2.circle(img, (cx, cy), cr, (15, 18, 214), -1)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
