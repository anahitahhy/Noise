import cv2
import numpy as np


img = cv2.imread('gu.png',0)
img=img/225

cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

x,y=img.shape
g= np.zeros((x,y), dtype = np.float32)

pepper = 0.1
salt = 1 - pepper
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
cv2.imshow('imag_noise', g)
cv2.waitKey(0)
cv2.destroyAllWindows()
from skimage import img_as_ubyte
cv2.imwrite('50%.jpg', img_as_ubyte(g))
