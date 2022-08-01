from pytube import Playlist, YouTube
from moviepy.editor import *

fpath = lambda x: './src/' + x

def ydown(url: str, prefix: str = ""):
    yt = YouTube(url)
    vpath = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)
        .order_by("resolution")
        .desc()
        .first()
        .download(output_path=fpath("video/"), filename_prefix=f"{prefix} ")
    )
    apath = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True)
        .order_by("abr")
        .desc()
        .first()
        .download(output_path=fpath("audio/"), filename_prefix=f"{prefix} ")
    )

    v = VideoFileClip(vpath)
    a = AudioFileClip(apath)

    v.audio = a
    v.write_videofile(fpath(f"1080/{vpath.split('/')[-1]}"))

def playlistdown(url: str, prefix: str = ""):
    pl = Playlist(url)
    for v in pl.video_urls:
        try:
            ydown(v, prefix)
        except:
            continue