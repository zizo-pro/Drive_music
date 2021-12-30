import pafy
from pydub import AudioSegment
from os import chdir , remove , listdir , rename , mkdir
import eyed3 
from shutil import move
from time import sleep
chdir("/media/ziad/Turbo/zizo/songs_before")
class mainapp():
    def __init__(self, parent=None):
        super(mainapp).__init__()
        self.getsonglink()

    def getsonglink(self):
        self.song_link = input("song link : ")
        self.s = pafy.new(self.song_link)
        self.song = self.s.getbestaudio(preftype="m4a")
        print(self.song)
        self.sze = self.song.get_filesize()
        self.size = str(self.sze/1024/1024)
        print(f"{self.size[:4]} MB")
        self.title = self.s.title
        self.author = self.s.author
        print(self.title.upper())
        print(self.author.upper())
        self.song.download()
        if "VEVO" in self.author.upper():
            self.m = self.author.upper().find("VEVO")
            self.author = self.author.upper()[:self.m]
        
        self.m4song = listdir()[0]
        self.m4songaf = self.m4song[:-4]
        self.mp3song = f"{self.m4songaf}.mp3"
        self.m4audio = AudioSegment.from_file(self.m4song , format="m4a")
        self.m4audio.export(f"{self.mp3song}" , format="mp3")

        remove(self.m4song)
        if "(" in self.title:
            mo1 = self.title.find("(")
            mo2 = self.title.find(")")
            moh = self.title[mo1:mo2+1]
            self.title = self.title[:mo1]

        if "|" in self.title:
            index = self.title.find("|")
            self.title = self.title[:index]

        file = eyed3.load(self.mp3song)
        file.tag.artist = self.author.upper()
        file.tag.album = self.author.upper()
        file.tag.album_artist = self.author.upper()
        file.tag.title = self.title.upper()
        file.tag.save()

        rename(self.mp3song,f"{self.title.upper()}.mp3")

        chdir("/media/ziad/Turbo/zizo/songs")

        current_files = listdir()

        if self.author.upper() in current_files:
            move(f"/media/ziad/Turbo/zizo/songs_before/{self.title.upper()}.mp3",f"/media/ziad/Turbo/zizo/songs/{self.author.upper()}/{self.title.upper()}.mp3")

        else:
            mkdir(f"/media/ziad/Turbo/zizo/songs/{self.author.upper()}")
            move(f"/media/ziad/Turbo/zizo/songs_before/{self.title.upper()}.mp3",f"/media/ziad/Turbo/zizo/songs/{self.author.upper()}/{self.title.upper()}.mp3")

song = mainapp()