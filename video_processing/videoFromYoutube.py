from pytube import YouTube
from pytube import Playlist

# download video in the url
# DOWNLOAD_FOLDER = r"C:\Users\kht96\Desktop\datasets\runway_videos"
# url_list = [r'https://www.youtube.com/watch?v=U69w7UPlsiM']
# for url in url_list:
#     yt = YouTube(url)
#     stream = yt.streams.get_highest_resolution()
#     stream.download(DOWNLOAD_FOLDER)

# download videos in the playlist
# DOWNLOAD_FOLDER = r"C:\Users\kht96\Desktop\datasets\videos"
# playlist_url = r'https://www.youtube.com/playlist?list=PL87Kw2WZi3N_aAX9x1cvvdCeJlYiwBo6q'
# p = Playlist(playlist_url)
# for video in p.videos:
#     video.streams.get_highest_resolution().download(DOWNLOAD_FOLDER)

import os
# from pytube import YouTube
# from pytube import Playlist

# download video in the url
# ----------------------------------------------------------------
url = r"https://www.youtube.com/watch?v=U1Yxhfo0fNg"
yt = YouTube(url)
original_folder = r"C:\Users\kht96\Desktop\datasets\runway_males"
original = yt.streams
for k, elem in enumerate(original,1) :
    save_dir = original_folder + str(k)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    elem.download(save_dir)