
import cv2
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]

img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("Original Size:", img.shape)

bigger = cv2.resize(img, None, fx=2, fy=2)
print("Bigger Size:", bigger.shape)

smaller = cv2.resize(img, None, fx=0.5, fy=0.5)
print("Smaller Size:", smaller.shape)

# Show separately with real figure sizes
plt.figure(figsize=(6,4))
plt.imshow(img)
plt.title("Original")
plt.axis("off")
plt.show()

plt.figure(figsize=(10,8))
plt.imshow(bigger)
plt.title("Bigger Image")
plt.axis("off")
plt.show()

plt.figure(figsize=(3,2))
plt.imshow(smaller)
plt.title("Smaller Image")
plt.axis("off")
plt.show()
