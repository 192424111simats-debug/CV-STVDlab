# ============================================
# 10. Homography Matrix Transformation
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

src_points = np.float32([
    [50,50],
    [cols-50,50],
    [50,rows-50],
    [cols-50,rows-50]
])

dst_points = np.float32([
    [20,100],
    [cols-100,50],
    [100,rows-20],
    [cols-50,rows-100]
])

H, status = cv2.findHomography(src_points, dst_points)

result = cv2.warpPerspective(img, H, (cols, rows))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(result)
plt.title("Homography Transformation")
plt.axis("off")
plt.show()
