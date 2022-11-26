# coding: UTF-8
# Arquivo: main

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from func import *
from threading import Thread
from time import sleep

yt_gen = yt()

class Main(FloatLayout):
    def get_video(self):
        video = yt_gen.set_url(self.ids.url.text)
        self.ids.thumbnail.source = video[0]
        self.ids.title.text = video[1]
        self.ids.quality.values = video[2]
        self.ids.download.disabled = False

    def download(self):
        thread = Thread(target=yt_gen.download, args=(self.ids.quality.text,), daemon=True)
        thread.run()

        while thread.is_alive():
            self.ids.download.disabled = True
            sleep(.5)

        self.ids.download.disabled = True
        self.ids.url.text = "Insert here the video link!"
        self.ids.thumbnail.source = "thumbplaceholder.jpg"
        self.ids.title.text = ""
        self.ids.quality.text = "Quality"
        yt_gen.reset()

class MainApp(App):
    Config.set('graphics', 'resizable', 0)
    Config.set('graphics', 'height', 550)
    Config.set('graphics', 'width', 850)

    def build(self):
        self.title = 'Youtube video downloader - By Lokost'
        return Main()

if __name__ == '__main__':
    MainApp().run()


# Fim