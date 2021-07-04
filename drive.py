import pafy
from pydub import AudioSegment
from os import chdir , remove , listdir , rename , mkdir
import eyed3 
from shutil import move

chdir("/media/ziad/92A816A5A81687BD/ZIZO/songs_before")

song_link = input("enter song link here: ")
song = pafy.new(song_link)
s = song.getbestaudio(preftype="m4a")
print(s)
size = s.get_filesize()
sze = str(size/1024/1024)
author = song.author
title = song.title
print(f"{sze[:4]} MB")

if "VEVO" in author.upper():
    m = author.upper().find("VEVO")
    author = author.upper()[:m]

print(title)
print(author.upper())

s.download()

m4song = listdir()[0]
m4songaf = m4song[:-4]

mp3song = f"{m4songaf}.mp3"

m4audio = AudioSegment.from_file(m4song , format="m4a")
m4audio.export(f"{mp3song}" , format="mp3")

remove(m4song)
if "(" in title:
    mo1 = title.find("(")
    mo2 = title.find(")")
    moh = title[mo1:mo2+1]
    title = title[:mo1]
# if "-" in title:
#     index = title.find("-")
#     title = title[:index]
if "|" in title:
    index = title.find("|")
    title = title[:index]

file = eyed3.load(mp3song)
file.tag.artist = author.upper()
file.tag.album = author.upper()
file.tag.album_artist = author.upper()
file.tag.title = title.upper()
file.tag.save()


rename(mp3song,f"{title.upper()}.mp3")

chdir("/media/ziad/92A816A5A81687BD/ZIZO/songs")

current_files = listdir()

if author.upper() in current_files:
    move(f"/media/ziad/92A816A5A81687BD/ZIZO/songs_before/{title.upper()}.mp3",f"/media/ziad/92A816A5A81687BD/ZIZO/songs/{author.upper()}/{title.upper()}.mp3")

else:
    mkdir(f"/media/ziad/92A816A5A81687BD/ZIZO/songs/{author.upper()}")
    move(f"/media/ziad/92A816A5A81687BD/ZIZO/songs_before/{title.upper()}.mp3",f"/media/ziad/92A816A5A81687BD/ZIZO/songs/{author.upper()}/{title.upper()}.mp3")