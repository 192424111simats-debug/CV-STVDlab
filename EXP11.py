#experiment 11

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]

img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, cols = img.shape[:2]

src = np.float32([
    [0, 0],
    [cols-1, 0],
    [0, rows-1],
    [cols-1, rows-1]
])

dst = np.float32([
    [80, 40],
    [cols-120, 80],
    [40, rows-80],
    [cols-60, rows-40]
])

H, status = cv2.findHomography(src, dst, method=0)

dlt_result = cv2.warpPerspective(img, H, (cols, rows))

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(dlt_result)
plt.title("DLT Transformation")
plt.axis("off")

plt.show()
