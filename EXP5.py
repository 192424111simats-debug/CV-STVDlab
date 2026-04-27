# ============================================
# 5. Rotation of Image
# Clockwise and Counter Clockwise
# ============================================

import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload Image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Read Image
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Rotate Image
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display Images
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(clockwise)
plt.title("Clockwise Rotation")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(counter_clockwise)
plt.title("Counter Clockwise Rotation")
plt.axis("off")

plt.show()
