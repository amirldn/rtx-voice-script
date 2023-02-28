
# rtx-voice-script

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![HitCount](http://hits.dwyl.com/amirmaula/rtx-acapella.svg)](http://hits.dwyl.com/amirmaula/rtx-acapella)

A python script that takes an input MP3/FLAC/MOV/MP4/WAV file and outputs an acapella version as a WAV using the power of NVIDIA's RTX Voice. Since RTX Voice is closed source, this records files in real-time so should be used for experimental purposes and for library overhauls.

## Getting Started

**Requirements**

 - A Windows PC running NVIDIA RTX Voice (GTX GPU's work fine for this using this [guide](https://www.windowscentral.com/how-enable-rtx-voice-all-nvidia-gpus-including-older-geforce-gtx-cards)) [https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/](https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/)
 - VB Audio (Virtual Cable) [https://vb-audio.com/Cable/index.htm](https://vb-audio.com/Cable/index.htm)
 - Python 3.9
 - [ffmpeg](https://ffmpeg.org/download.html) add FFmpeg to the System Variables ([install help](docu/install_ffmpeg.md))

---

## Steps

### 💻+🐍 anaconda

Anaconda is an open source distribution for the Python programming language. The Anaconda distribution includes many of the most commonly used Python libraries by default, also a user interface for managing and updating packages.

You can create your own working environment so that, depending on the project, you can use different dependencies packages.

1. install [anaconda](https://www.anaconda.com/)
1. open anaconda terminal
1. ⌨️=``conda create -n rtx-voice python=3.9`` create working environment
1. ⌨️=``conda activate rtx-voice``
1. 🖥️=``(base) C:\Users\UserName>``  ⌨️=``D:`` If you want to have the project in another location on the hard disk. Change partion.
1. 🖥️=``(base) D:\>``  ⌨️=``cd D:\Folder\Folder`` change path

---

### 💻 Use and Download the tool

1 ) Clone the repository and cd into it

```
git clone https://github.com/amirmaula/rtx-voice-script.git
```

2 ) Install the prerequisites via

```
pip install -r requirements.txt
```

3 ) Set RTX Voice's microphone input to your VB Audio Cable (Virtual AUX)

4 ) To execute the program, run it in your CLI like so:

```
python ./rtx-core.py -i [input path] -o [file directory & name for output]
```

For example **input defined** (automatically creates output file)

```
python rtx-core.py -i "D:\UserName\Video\video.mov"
```

For example single **input defined** and **output defined** (not testet)
```
python ./rtx-core.py -i song.flac -o D:\Music\Acapella\cool_song.wav
```


5 ) Follow the on screen prompts.

![VirtualCable](docu/selection_VirtualCableForOutput.jpg)

just the number ``5``

![NvidiaBrodcast](docu/selection_NvidiaBrodcastForRecording.jpg)

just the number ``3``

6 ) Your new config file will then be exported to code's directory.

---

## 🎬 sync tool
I always had the problem on my computer that there was a small time lag. This depends on the start time of the audio recording and the start time of the recording and there is always a small time difference.

[python-warpdrive](https://github.com/dsholes/python-warpdrive) syncs to source audio from video with the filter audio and returned time offset. Nice Tool for this Job is from [🧙‍♂️ Darren Sholes](https://github.com/dsholes).

---

## 🔧 To-do

- ~~Add FLAC support~~ **DONE**
- ~~Create and load config file so that the user does not need to select input/output everytime~~ **DONE**
- ~~Add a real-time timer of how long a file has been playing for~~ **DONE**
- Add GUI

---

## Known Issues

- Sometimes the config file will get messed up so just delete the config.cfg
- The code will crash if the folder you wish to export your .wav to does not already exist, so just create the folder beforehand and it will save with no issues

- Results may vary with this and you can tweak the noise suppression to what works for you. This can be used for songs and speech etc.

- This is work in progress and I am somewhat an amateur when it comes to coding so any improvements made to the code and constructive criticism is greatly appreciated.

- NVIDIA RTX is propriety software and belongs to NVIDIA and all rights are reserved. This program uses the NVIDIA RTX software as intended and does not use any exploitation.

- An audio driver(**nahimic**) from my laptop(msi) interfered with my virtual audio cable and i had to close it befor i could use the virtual audio cable.

## Other Solutions (VST Plugins)

You can use VST plugin for Adobe Audition, Adobe Premiere Pro or Audacity. There is this youtube tutorial [from TroubleChute](https://www.youtube.com/watch?v%3DSMx3_mK59ww)

A Cheap solution is to use a VST plugin called [ELGATO AUDIO EFFECTS](https://www.elgato.com/de/downloads) which is a free plugin and you can download it from elgato website. The Last time I checked it does not work when you press export. It gave me audio artefacts.

The VST [voicefx](https://www.xaymar.com/projects/voicefx/) cost money for more advanced features. Nvidia list this VST plugin [here](https://www.nvidia.com/de-de/geforce/broadcasting/broadcast-sdk/resources/).

---

## Notes

### ffmpeg

- ``ffmpeg -i input.wav -vn -ar 48000 -ac 2 -b:a 192k output.mp3``

### pip

- pip check version install from requirements ``pip show mutagen``
- for installation ``pip install mutagen``

### conda

- ``conda create -n rtx-voice python=3.9``
- ``conda activate rtx-voice``
- ``conda deactivate``

- ``rtx-core.py -i audio.flac -o D:\AudioKI\audio-d.wav````