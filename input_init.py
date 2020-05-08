import time
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name #Get playback device names
from pygame import mixer #Playing sound
mixer.init() #Initialize the mixer, this will allow the next command to work
speakerDevices = [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))] #Returns playback devices
print(speakerDevices)
mixer.quit() #Quit the mixer as it's initialized on your main playback device
mixer.init(devicename=speakerDevices[1]) #Initialize it with the correct device
mixer.music.load("gp.mp3") #Load the mp3
mixer.music.play() #Play it
time.sleep(30)