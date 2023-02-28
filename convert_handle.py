import sys
import os
import subprocess

def convert_to_mp3(input_filename, output_filename=None):
    if output_filename is None:
        output_filename = input_filename.rsplit(".", 1)[0] + ".mp3"

    command = [
        "ffmpeg",
        "-i", input_filename,
        "-vn",          # No Video/No Cover Art
        "-ar", "48000", # Sample Rate
        "-ac", "1",     # Channels
        "-b:a", "256k", # Bitrate
        "-shortest",    # Shortest Stream
        output_filename
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f'Error: {stderr.decode()}')
        return False, None
    else:
        print(f'Success: {stdout.decode()}')
        return True , output_filename

"""
How to Use:
input_filename = "input.mp4"
success, output_filename = convert_to_mp3(video.mp4)
"""



# This function is used to merge the audio and video streams of a video file
# Todo: Problem with the audio stream, is not perfect in sync with the video

def merge_video_audio(video_file, audio_file):
    base_path, ext = os.path.splitext(video_file)
    output_file = base_path + "_rtxFilter" + ext
    command = [
        "ffmpeg",
        "-i", video_file,   # Video File Clip A
        "-i", audio_file,   # Audio File Clip A (with Filter)
        "-map", "0:v",      # Map Video Stream
        "-map", "1:a",      # Map Audio Stream
        "-c:v", "copy",     # Copy Video Stream (lossless)
        "-c:a", "aac",      # Copy Audio Stream
        "-b:a", "256k",     # Bitrate (HQ)
        "-shortest",        # Shortest Stream
        output_file
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f'Error: {stderr.decode()}')
        return False
    else:
        print(f'Success: {stdout.decode()}')
        return True , None

def trim_audio(audio_file, shift_in_ms):
    output_file = audio_file.rsplit(".", 1)[0] + "_trim.wav"
    command = [
        "ffmpeg",
        "-ss", shift_in_ms, # Start Time as string with ms
        "-i", audio_file,   # Audio File Clip A (with Filter)
        "-c", "copy",       # Copy Audio Stream
        output_file
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f'Error: {stderr.decode()}')
        return None
    else:
        print(f'Success: {stdout.decode()}')
        return output_file

