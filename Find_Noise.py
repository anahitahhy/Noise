import numpy as np, cv2
from matplotlib import pyplot as plt
img = cv2.imread('mo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 20, 20, 14, 42)
cv2.imwrite('mo_out.jpg', cv2.cvtColor(dst, cv2.COLOR_RGB2BGR))
plt.subplot(121); plt.imshow(img)
plt.subplot(122); plt.imshow(dst)
plt.show()
