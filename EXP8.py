# ============================================
# 8. Perspective Transformation on Image
# ============================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]

img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, cols = img.shape[:2]

pts1 = np.float32([[50,50], [cols-50,50], [50,rows-50], [cols-50,rows-50]])
pts2 = np.float32([[0,0], [cols,50], [50,rows], [cols-50,rows-50]])

M = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(img, M, (cols, rows))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(perspective)
plt.title("Perspective Transformation")
plt.axis("off")
plt.show()
