#!/usr/bin/env python3

from pytube.cli import on_progress
from pytube import YouTube
import time
from hurry.filesize import alternative, size
import sys


def main():
    link = sys.argv[1]
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams
    video_size = size(ys.first().filesize, system=alternative)

    print_video_information(yt.title, yt.views, yt.length, video_size)
    download_video(ys)


def print_video_information(title, views, video_length, file_size):
    print("Title: ", title)
    print("Number of views: ", views)
    print("Length of video: ", time.strftime('%H:%M:%S', time.gmtime(video_length)))
    print('File Size: ', file_size)


def download_video(youtube_stream):
    # Starting download
    youtube_stream.get_highest_resolution().download()
    print("\nDownload completed!!")


if __name__ == "__main__":
    main()
