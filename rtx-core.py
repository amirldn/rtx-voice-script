import time
import sys
import getopt
import os
import time

from mutagen.mp3 import MP3
from mutagen.flac import FLAC

from input_handle import *
from record_handle import *
from convert_handle import *
from sync_handle import *

# addTimepaddding
addTimepaddding = 5 # seconds


# This is the main function that is called when the program is run
def main(argv):
    input_song_path, export_song_path = arguments(argv)

    input_file_extension = get_file_extension(input_song_path)
    # Check Input File Type
    if "mp3" in input_file_extension.lower():
        codec = "MP3"
        convert = False
    elif "flac" in input_file_extension.lower():
        codec = "FLAC"
        convert = False
    elif "mov" in input_file_extension.lower():
        codec = "MP3"
        convert = True
    elif "mp4" in input_file_extension.lower():
        codec = "MP3"
        convert = True
    elif "wav" in input_file_extension.lower():
        codec = "MP3"
        convert = True

    # Convert the input file to MP3 if it is not already
    if convert == True:
        convert_success, convert_filename = convert_to_mp3(input_song_path)
        if convert_success == False:
            sys.exit()
        else:
            orginal_filename = input_song_path # Save the original filename for later StreamCopy
            input_song_path = convert_filename

    if check_cfg_exists() == False:
        print("Config file not found... creating")
        mixer.init(devicename=select_speaker_output())
        #devicename = select_speaker_output()
        mic_input = choose_rtx_output()
    else:
        print("Read Config file...")
        mixer.init(devicename=cfg_read("speaker_output"))
        mic_input = int(cfg_read("mic_input"))
    
    # Load the song into the mixer for playback
    mixer.music.load(input_song_path)
    
    # Get the length of the song for the record function
    if codec == "MP3":
        input_track = MP3(input_song_path)
    elif codec == "FLAC":
        input_track = FLAC(input_song_path)
    
    length_of_input_song = int(input_track.info.length)
    hours, mins, seconds = convertTime(length_of_input_song)
    bitrate_of_input_song = int(input_track.info.sample_rate)
    sample_rate_input_song = int(input_track.info.sample_rate)

    # Print some info about the song to the console
    print("\nNow Processing: " + input_song_path + "\n")
    print("SampleRat: " + str(bitrate_of_input_song))
    print('Duration: %s:%s:%s' % (hours, mins, seconds))
    print("Playbacktime is in Realtime, this tool tunnels the audio to the RTX Voice Input")
    print("Endtime: " + add_time(hours, mins, seconds))
    mixer.music.play()  # Play it
    # Record it
    record(
    length_of_input_song+addTimepaddding,
    export_song_path,
    mic_input,
    bitrate_of_input_song
    )
    mixer.music.stop()  # Stop it
    mixer.quit()  # Quit it

    print("if you hear audio artifacts, try to restart the brodcast,read the manual")
    # check if input_file_extension is mp4 or mov
    if "mov" in input_file_extension.lower() or "mp4" in input_file_extension.lower():
        # Sync the recorded audio with the input audio
        isSync = input("\nYou can still sync the audio track with another tool. Do you want to try this in this tool? y/n: ")
        if(isSync.lower() == "y"):
            # get the syncs tool
            getSyncsTool()
            # preparation for synchronization
            folderName = get_file_name(orginal_filename)+"_sync"
            folderSync = create_folder(orginal_filename, folderName)
            mv_files(folderSync, input_song_path, export_song_path)
            # run the sync tool
            runSycTool(folderSync)
            jsonFile = os.path.join((folderSync+"\\") + "_warpdrive_results", "_warpdrive_"+folderName+".json") # i hate windows paths
            #jsonFile = jsonFile.replace("\\", "/")
            print("jsonFilePath: " + jsonFile)
            time.sleep(2)
            json = extract_values_from_json(jsonFile, key_list)
            # get the sync value
            shiftIndex = find_index_of_shift(json)
            shiftOffset = json[0]["tshift_from_base_sec"]
            # convert s in ms
            shiftOffset = shiftOffset * 1000
            shiftOffset = str(shiftOffset)+"ms"
            # get the audio file
            audioRTX = os.path.join(folderSync, (get_file_name(export_song_path)+".wav"))
            audioRTX_trim = trim_audio(audioRTX, shiftOffset)
            if audioRTX_trim == None:
                print("Error: Audio Trim Failed")
                sys.exit()
            else:
                mergStatus = merge_video_audio(orginal_filename, audioRTX_trim)
                if mergStatus == False:
                    print("Error: Merge Failed")
                    sys.exit()
                else:
                    print("Merge Success")
            

main(sys.argv[1:])
