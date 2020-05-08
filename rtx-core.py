import time
import sys
import getopt

from mutagen.mp3 import MP3

from input_handle import *
from record_handle import *

def main(argv):
    input_song_path, export_song_path = arguments(argv)
    mixer.init(devicename=select_speaker_output())
    mic_input = choose_rtx_output()
    print(input_song_path)
    mixer.music.load(input_song_path)
    mp3_track = MP3(input_song_path)
    length_of_mp3 = int(mp3_track.info.length)
    hours, mins, seconds = convert(length_of_mp3)
    print("\nNow Playing: " + input_song_path + "\n")
    print('Duration: %s:%s:%s' % (hours, mins, seconds))
    mixer.music.play()  # Play it
    record(length_of_mp3, export_song_path,mic_input)
    time.sleep(length_of_mp3)

main(sys.argv[1:])
