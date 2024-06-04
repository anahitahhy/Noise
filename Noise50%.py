import cv2
import numpy as np


img = cv2.imread('bild.jpg', cv2.IMREAD_GRAYSCALE)


rader, kolumner = img.shape

brus_indices = np.random.choice(rader * kolumner, int(0.5 * rader * kolumner), replace=False)


brus = np.random.choice([0, 255], int(0.1 * rader * kolumner))


img_brus = img.copy()
img_brus.flat[brus_indices] = brus


img_brus = img_brus / 255.0

img_brus[img_brus < 0.05] = 0
img_brus[img_brus > 0.95] = 1


img_brus = (img_brus * 255).astype(np.uint8)

cv2.imwrite('brusig_bild.jpg', img_brus)