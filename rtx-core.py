import time
import sys
import getopt

from mutagen.mp3 import MP3
from mutagen.flac import FLAC

from input_handle import *
from record_handle import *

def main(argv):
    input_song_path, export_song_path = arguments(argv)
    if "mp3" in input_song_path.lower():
        codec = "MP3"
    else:
        codec = "FLAC"
    if check_cfg_exists() == False:
        # print("Config file not found... creating")
        mixer.init(devicename=select_speaker_output())
        mic_input = choose_rtx_output()
    else:
        mixer.init(devicename=cfg_read("speaker_output"))
        # mixer.init(devicename=select_speaker_output())
        mic_input = choose_rtx_output()
    print(input_song_path)
    mixer.music.load(input_song_path)
    if codec == "MP3":
        input_track = MP3(input_song_path)
    else:
        input_track = FLAC(input_song_path)
    length_of_input_song = int(input_track.info.length)
    hours, mins, seconds = convert(length_of_input_song)
    bitrate_of_input_song = int(input_track.info.sample_rate)

    print("\nNow Playing: " + input_song_path + "\n")
    print("Bitrate: " + str(bitrate_of_input_song))
    print('Duration: %s:%s:%s' % (hours, mins, seconds))
    mixer.music.play()  # Play it
    record(length_of_input_song, export_song_path,mic_input,bitrate_of_input_song)

main(sys.argv[1:])
