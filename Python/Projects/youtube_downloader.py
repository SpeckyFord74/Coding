from pytube import YouTube
from sys import argv

try:
    link = argv[1]
except ValueError:
    print("Please enter a link!")

yt = YouTube(link)

print("Title: ", yt.title)
print(f"Views: {yt.views}")

yd = yt.streams.get_highest_resolution()
yd.download("~/Coding/Python/Projects")