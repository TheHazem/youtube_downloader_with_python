from pytube import YouTube

YT = YouTube(input("-- Please copy and paste the video URl here --"))

# print(YT.title)

# print(YT.thumbnail_url)

# print(YT.description)

# print(YT.views)



YT.streams.get_lowest_resolution().download(filename="HAHAHAHA")