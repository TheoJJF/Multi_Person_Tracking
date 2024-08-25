import os
import supervision as sv

from supervision.assets import VideoAssets, download_assets

# Create 'video_demo/' directory if 'video_demo/' directory does not exist.
if not os.path.exists('video_demo'):
    os.makedirs('video_demo')

# Change directory to 'video_demo' for video download.
os.chdir('video_demo')

# Download video.
download_assets(VideoAssets.PEOPLE_WALKING)

# Error with original file name, change file name to 'demo_vid.mp4'.
os.rename('people-walking.mp4', 'demo_vid.mp4')
