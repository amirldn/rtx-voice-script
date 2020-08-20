import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
import sys
import getopt
import json


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    if len(str(hours)) == 1:
        hours = "0"+str(hours)
    if len(str(mins)) == 1:
        mins = "0"+str(mins)
    if len(str(seconds)) == 1:
        seconds = "0"+str(seconds)
    return hours, mins, seconds

def check_cfg_exists():
    if os.path.isfile('./config.cfg'):
        return True
    else:
        return False

def create_cfg():
    cfg = open("config.cfg", "w+")
    print("Config Created")
    cfg.close()

def cfg_write(variable_name, value):
    cfg = open("config.cfg", "a")
    json.dump([str(variable_name), str(value)], cfg)
    cfg.write("\n")
    cfg.close()

def cfg_read(variable_name):
    cfg = open("config.cfg", "r")
    cfg_list = json.load(cfg)
    print(str(cfg_list))
    if cfg_list[0] == variable_name:
        return cfg_list[1]
    # try:
    #     cfg = open("config.cfg", "r")
    #     cfg_list = json.load(cfg)
    #     print(str(cfg_list))
    #     if cfg_list[0] == variable_name:
    #         return cfg_list[1]
    # except:
    #     print("Failed to load config file, falling back")
    #     return select_speaker_output()

def select_speaker_output():
    if not check_cfg_exists():
        create_cfg()
    print("--- SPEAKER OUTPUT ---")
    mixer.init()
    speakerDevices = [
        get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))
    ]
    mixer.quit()
    # print(speakerDevices)
    for i in speakerDevices:
        if ("AUX" or "Stereo Mix") in i:
            print("\nUsing " + i)
            valid = input("Is this correct (y/n)?  ")
            if valid.lower() == "y":
                return speakerDevices[speakerDevices.index(i)]
    print("\nCould not find VB Audio AUX")

    loop_count = 0
    print("\nAudio Options: ")
    for i in speakerDevices:
        print(str(loop_count) + ".", i)
        loop_count += 1
    print("\nIf VB Audio is not found here, please check it is not disabled.")
    speaker_choice = input("\nPlease select the VB Audio speaker input: ")
    cfg_write("speaker_output", speakerDevices[int(speaker_choice)])
    return speakerDevices[int(speaker_choice)]

    return None

def song_select():
    import easygui
    selected_file=easygui.fileopenbox()
    print(selected_file)
    return selected_file

def arguments(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('rtx-core.py -i <file input path> -o <file name for output>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('rtx-core.py -i <file input path> -o <file name for output>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if outputfile == '':
        outputfile = "rtx-export"
    if inputfile == '':
        print ('rtx-core.py -i <file input path> -o <file name for output>')
        sys.exit(2)
    # print ('Input file is', inputfile)
    # print ('Output file is', outputfile)
    return inputfile,outputfile
