from pytube import YouTube

link = 'https://www.youtube.com/watch?v=Kee9Et2j7DA'  # input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
