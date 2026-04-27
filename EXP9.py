# ============================================
# 9. Perspective Transformation on Video
# Colab Working Version
# ============================================

import cv2
import numpy as np
from google.colab import files
from IPython.display import HTML, display
from base64 import b64encode

# Upload video
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

cap = cv2.VideoCapture(video_path)

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 25

temp_output = "temp_output.mp4"
final_output = "perspective_video.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_output, fourcc, fps, (width, height))

# Strong perspective transformation points
pts1 = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

pts2 = np.float32([
    [100, 0],
    [width-100, 50],
    [50, height-50],
    [width, height]
])

M = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    transformed = cv2.warpPerspective(frame, M, (width, height))
    out.write(transformed)

cap.release()
out.release()

# Convert to playable MP4 format
!ffmpeg -y -i temp_output.mp4 -vcodec libx264 perspective_video.mp4

# Display video in Colab
mp4 = open(final_output, "rb").read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

display(HTML(f"""
<video width="600" controls>
  <source src="{data_url}" type="video/mp4">
</video>
"""))
