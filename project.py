#!/usr/bin/env python3

import sys
import time

from hurry.filesize import alternative, size
from pytube import YouTube
from pytube.cli import on_progress


def main():
    link = sys.argv[1]
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams
    video_size = size(ys.first().filesize, system=alternative)

    print_video_information(yt.title, yt.views, yt.length, video_size)
    download_video(ys)


def print_video_information(title, views, video_length, file_size):
    """Prints the video title, number of views, lengths and its size in MB."""
    print("Title: ", title)
    print("Number of views: ", views)
    print("Length of video: ", time.strftime('%H:%M:%S', time.gmtime(video_length)))
    print('File Size: ', file_size)


def download_video(youtube_stream):
    """Starting download the video, and shows when it is done."""
    youtube_stream.get_highest_resolution().download()
    print("\nDownload completed!!!")


if __name__ == "__main__":
    main()
