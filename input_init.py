import time
from mutagen.mp3 import MP3
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds


def select_speaker_output():
    mixer.init()
    speakerDevices = [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
    mixer.quit()
    # print(speakerDevices)
    for i in speakerDevices:
        if "AUX" in i:
            print("\nUsing "+i)
            valid = input("Is this correct (y/n)?  ")
            if valid.lower() == "y":
                return speakerDevices[speakerDevices.index(i)]
    print("\nCould not find VB Audio AUX.")

    loop_count = 0
    print("\nAudio Options: ")
    for i in speakerDevices:
        print(str(loop_count)+".",i)
        loop_count+=1

    print("\nIf VB Audio is not found here, please check it is not disabled.")
    speaker_choice=input("\nPlease select the VB Audio speaker input: ")
    return speakerDevices[int(speaker_choice)]

    return None



mixer.init(devicename=select_speaker_output())
songName = "./gp.mp3"
mixer.music.load(songName)
mp3_track = MP3(songName)
length_of_mp3 = int(mp3_track.info.length)
hours, mins, seconds = convert(length_of_mp3)
print("\nNow Playing: "+ songName+"\n")
print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", seconds)


mixer.music.play() #Play it
time.sleep(length_of_mp3)