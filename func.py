# coding: UTF-8
# Arquivo: func

from pytube import YouTube
from os.path import exists
from os import mkdir, system

class yt:
    def __init__(self) -> None:
        if not exists('./Downloaded videos'):
            mkdir('./Downloaded videos')
        self.path = './Downloaded videos'

    def set_url(self, link: str):
        self.url = YouTube(link)
        self.video = self.url.streams
        self.video_title = self.video.first().title

        qualities = list(dict.fromkeys([i.resolution for i in self.video.filter(type='video')]))
        qualities.sort(reverse=True)
        try:
            qualities.remove('1080p') # This remove the Full HD option because is taking so long to download and makes the software stop responding for a while
        except ValueError:
            pass

        return [self.url.thumbnail_url, self.video.first().title, qualities]

    def download(self, quality: str):
        path = self.video.filter(res=quality).first().download(output_path=self.path)
        system(f'"{path}"')

    def reset(self):
        self.video = None
        self.url = None
        self.video_title = None

# Fim