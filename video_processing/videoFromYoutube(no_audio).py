from pytube import YouTube

url = r'https://www.youtube.com/watch?v=OANMHhMdUqs'
prefix = 'taemin'
save_path = r''

yt = YouTube(url)
yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)\
.order_by("resolution")\
.desc()\
.first()\
.download(output_path=save_path, filename_prefix=f"{prefix} ")