import wave

import pyaudio

from input_handle import cfg_write


def choose_rtx_output():
    print(" --- RTX INPUT ---")
    pyaudio_rtx_instance = pyaudio.PyAudio()
    info = pyaudio_rtx_instance.get_host_api_info_by_index(0)
    numdevices = info.get("deviceCount")
    for i in range(0, numdevices):
        if (
            pyaudio_rtx_instance.get_device_info_by_host_api_device_index(0, i).get(
                "maxInputChannels"
            )
        ) > 0:
            device = pyaudio_rtx_instance.get_device_info_by_host_api_device_index(
                0, i
            ).get("name")
            # print("Input ID ", i, " - ", device)
            if "NVIDIA RTX Voice" in device:
                print("\nUsing " + device)
                pyaudio_rtx_instance.terminate()
                cfg_write("mic_input", str(i))
                return i

                # Re-enable to have valid check for the RTX Mic
                # valid = input("Is this correct (y/n)?  ")
                # if valid.lower() == "y":
                #     pyaudio_rtx_instance.terminate()
                #     return i

    # If RTX not found then
    print("\n Could not find NVIDIA RTX Microphone.\n")
    print("Audio Options: ")
    for i in range(0, numdevices):
        if (
            pyaudio_rtx_instance.get_device_info_by_host_api_device_index(0, i).get(
                "maxInputChannels"
            )
        ) > 0:
            device = pyaudio_rtx_instance.get_device_info_by_host_api_device_index(
                0, i
            ).get("name")
            print( str(i)+ ".", device)

    print("\nIf RTX Microphone is not found here, please check it is not disabled and is installed correctly.")
    microphone_choice = input("\nPlease select the RTX Microphone input to record: ")
    cfg_write("mic_input", str(microphone_choice))
    return int(microphone_choice)


def record(length=10, user_output_name="file", mic_input='',bitrate_input=48000):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = bitrate_input
    CHUNK = 1024
    RECORD_SECONDS = length

    if ".wav" not in user_output_name:
        WAVE_OUTPUT_FILENAME = user_output_name + ".wav"
    else:
        WAVE_OUTPUT_FILENAME = user_output_name


    pyaudio_inst = pyaudio.PyAudio()

    # start Recording
    stream = pyaudio_inst.open(
        format=FORMAT,
        channels=CHANNELS,
        input_device_index=mic_input,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )
    print("Recording to RAM...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("\nWriting to .wav...")

    # Stop recording
    stream.stop_stream()
    stream.close()
    pyaudio_inst.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(pyaudio_inst.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b"".join(frames))
    waveFile.close()
    print("Complete!\n")
    print("Written to " + WAVE_OUTPUT_FILENAME)
    return None
