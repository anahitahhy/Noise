import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("ari.jpg",0)
def add_salt_and_pepper_noise(image, imp_noise =0.25):
    imp_noise=np.zeros((640,480),dtype=np.uint8)
    cv2.randu(imp_noise,0,255)
    imp_noise=cv2.threshold(imp_noise,245,255,cv2.THRESH_BINARY)[1]
    in_img= cv2.add(img,imp_noise)
    return in_img

fig=plt.figure(dpi=300)

fig.add_subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,3,2)
plt.imshow(imp_noise,cmap='gray')
plt.axis("off")
plt.title("Impulse Noise")

fig.add_subplot(1,3,3)
plt.imshow(in_img,cmap='gray')
plt.axis("off")
plt.title("Combined")