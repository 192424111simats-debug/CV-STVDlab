# ============================================
# 6. Moving Image from One Place to Another
# Translation Transformation
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

# Move Right = 100 px, Down = 50 px
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv2.warpAffine(img, M, (cols, rows))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(translated)
plt.title("Moved Image")
plt.axis("off")
plt.show()
