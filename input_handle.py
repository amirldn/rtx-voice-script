import os
import os.path
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
import getopt
import json
import configparser

from pygame import mixer
import pygame
import pygame._sdl2.audio as sdl2_audio
from typing import Tuple
import datetime

cfg = configparser.ConfigParser()


def convertTime(seconds):
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

def add_time(h, m, s):
    now = datetime.datetime.now()
    new_time = now + datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    return new_time.strftime("%H:%M:%S")

def check_cfg_exists():
    if os.path.isfile('./config.cfg'):
        return True
    else:
        return False

def cfg_create():
    with open('config.cfg', 'w') as cfg_file:
        cfg['AUDIO DEVICES'] = {'speaker_output': ''}
        cfg.write(cfg_file)

def cfg_write(variable_name, value):
    with open('config.cfg', 'w') as cfg_file:
        cfg['AUDIO DEVICES'][variable_name] = value
        cfg.write(cfg_file)

def cfg_read(variable_name):
    try:
        cfg.read('config.cfg')
        return cfg['AUDIO DEVICES'][variable_name]
    except:
        print("Failed to load config file, falling back")
        return select_speaker_output()

def get_devices(capture_devices: bool = False) -> Tuple[str, ...]:
    init_by_me = not pygame.mixer.get_init()
    if init_by_me:
        pygame.mixer.init()
    devices = tuple(sdl2_audio.get_audio_device_names(capture_devices))
    if init_by_me:
        pygame.mixer.quit()
    return devices

def select_speaker_output():
    if not check_cfg_exists():
        cfg_create()
    print("--- SPEAKER OUTPUT ---")
    speakerDevices = list(get_devices())
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


# function need upgrade for video file support
def arguments(argv):
    inputfile = ''
    outputfile = ''
    reset = 0

    # parse arguments
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError as err:
        print ('rtx-core.py -i <file input path> -o <file name for output>')
        print (str(err))
        sys.exit(2)
    # set variables from arguments if present else set to default values or help message
    for opt, arg in opts:
        if opt == '-h':
            print ('rtx-core.py -i <file input path> -o <file name for output>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    # after parsing arguments, check if inputfile is set, if not, exit
    if outputfile == '':
        outputfile = add_suffix_to_stem(inputfile, "rtx")
        outputfile = change_file_extension(outputfile, "wav")
    if inputfile == '':
        print("\n--- Input file missing ---\n")
        print ('rtx-core.py -i <file input path> -o <file name for output>')
        sys.exit(2)
    return inputfile,outputfile


# small function for file name/path manipulation

def add_suffix_to_stem(file_path, suffix):
    base_path, ext = os.path.splitext(file_path)
    return base_path + "_" + suffix + ext

def change_file_extension(file_path, new_extension):
    base_path, ext = os.path.splitext(file_path)
    return base_path + "." + new_extension

def get_file_extension(file_path):
    base_path, ext = os.path.splitext(file_path)
    return ext

def get_file_name(file_path):
    base_path, ext = os.path.splitext(file_path)
    return os.path.basename(base_path)
