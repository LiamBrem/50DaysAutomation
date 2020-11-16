from pytube import YouTube

SAVE_PATH = "C:\\Users\\liame"

link = input("link: ")

yt = YouTube(link)
print(yt.title)
cont = input("is this correct? (y/n)")
if cont == 'y':
    download()
else:
    exit()


def download():
    video = yt.streams.first()
    video.download(SAVE_PATH)
