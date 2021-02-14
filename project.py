from pytube import YouTube
import time
from progress.bar import Bar
from hurry.filesize import alternative, size

link = 'https://www.youtube.com/watch?v=Kee9Et2j7DA'  # input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)
ys = yt.streams
video_size = ys.first().filesize

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", time.strftime('%H:%M:%S', time.gmtime(yt.length)))
print('File Size: ', size(video_size, system=alternative))

# Starting download
print("Downloading...")
ys.get_highest_resolution().download()
print("Download completed!!")


