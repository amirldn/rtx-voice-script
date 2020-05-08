import time
from input_handle import *
from record_handle import *
from mutagen.mp3 import MP3

mixer.init(devicename=select_speaker_output())
song_name = "bibo.mp3"
song_path = "./"+song_name
print(song_path)
mixer.music.load(song_path)

mp3_track = MP3(song_path)
length_of_mp3 = int(mp3_track.info.length)
hours, mins, seconds = convert(length_of_mp3)
print("\nNow Playing: " + song_path + "\n")
print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", seconds)

mixer.music.play()  # Play it
record(length_of_mp3, song_name)
time.sleep(length_of_mp3)