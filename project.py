#!/usr/bin/env python3

from pytube.cli import on_progress
from pytube import YouTube
import time
from hurry.filesize import alternative, size
import sys

link = sys.argv[1]
yt = YouTube(link, on_progress_callback=on_progress)
ys = yt.streams
video_size = ys.first().filesize

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", time.strftime('%H:%M:%S', time.gmtime(yt.length)))
print('File Size: ', size(video_size, system=alternative))

# Starting download
#print("Downloading...")
ys.get_highest_resolution().download()
print("Download completed!!")
