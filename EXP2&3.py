# ============================================
# Video Processing in Google Colab
# Normal / Slow / Fast Motion
# ============================================

import cv2
from google.colab import files
from IPython.display import HTML, display
from base64 import b64encode

# --------------------------------------------
# Upload Video
# --------------------------------------------
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

# --------------------------------------------
# Function to Display Video in Colab
# speed:
# 1.0 = normal
# 0.5 = slow
# 2.0 = fast
# --------------------------------------------
def show_video(video_path, speed=1.0):
    video_file = open(video_path, "rb").read()
    video_url = "data:video/mp4;base64," + b64encode(video_file).decode()

    html_code = f"""
    <video width="640" controls playbackRate="{speed}">
      <source src="{video_url}" type="video/mp4">
    </video>
    <script>
      var v = document.querySelector("video");
      v.playbackRate = {speed};
    </script>
    """
    display(HTML(html_code))

# --------------------------------------------
# Normal Speed
# --------------------------------------------
print("Normal Speed Video")
show_video(video_path, speed=1.0)

# --------------------------------------------
# Slow Motion
# --------------------------------------------
print("Slow Motion Video")
show_video(video_path, speed=0.5)

# --------------------------------------------
# Fast Motion
# --------------------------------------------
print("Fast Motion Video")
show_video(video_path, speed=2.0)
