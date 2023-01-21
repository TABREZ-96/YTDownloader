from pytube import YouTube

link = "https://youtu.be/nWbj7W_pD9U"
youtube_1 = YouTube(link)

print(youtube_1.title)

print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() #all Format

videos = youtube_1.streams.filter(only_audio=True) #Only Audio
vid = list(enumerate(videos))
for i in vid :
    print(i)
print()
strm = int(input("Enter :"))
videos[strm].download()
print('Succesfully')



#***** PLAYLIST **********

from pytube import Playlist

py = Playlist("Paste PlayList URL")
print(f'Downlaoding: {py.title}')

for vedio in py.vedios:
    vedio.streams.first().download()

