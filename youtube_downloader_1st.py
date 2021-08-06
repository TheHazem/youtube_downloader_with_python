from pytube import YouTube

YT = YouTube(input("-- Please copy and paste the video URl here --"))

print(YT.title)

print(YT.thumbnail_url)

print(YT.description)

print(YT.views)
# to get the lowest youtube video resolution
YT.streams.get_lowest_resolution().download(filename="lowest")
# ##################################################################
# to get video title
print(YT.title)
# to get video thumbnail photo
print(YT.thumbnail_url)
# to get video description
print(YT.description)
# to get video views
print(YT.views)
# to get the highest youtube video resolution
YT.streams.get_highest_resolution().download(filename="High")
