import pyaudio
import wave

def choose_rtx_output():
    pyaudio_rtx_instance = pyaudio.PyAudio()

    info = pyaudio_rtx_instance.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (pyaudio_rtx_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            device = pyaudio_rtx_instance.get_device_info_by_host_api_device_index(0, i).get('name')
            # print("Input ID ", i, " - ", device)
            if "NVIDIA RTX Voice" in device:
                pyaudio_rtx_instance.terminate()
                return i



def record(length=10,song_name="file"):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = length
    WAVE_OUTPUT_FILENAME = song_name+".wav"

    pyaudio_instance = pyaudio.PyAudio()

    # start Recording
    stream = pyaudio_instance.open(format=FORMAT, channels=CHANNELS, input_device_index = choose_rtx_output(),
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print ("recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    pyaudio_instance.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(pyaudio_instance.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    return None