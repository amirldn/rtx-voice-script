
# rtx_acapella
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![HitCount](http://hits.dwyl.com/amirmaula/rtx-acapella.svg)](http://hits.dwyl.com/amirmaula/rtx-acapella)



A python script that takes an input MP3/FLAC file and outputs an acapella version as a WAV using the power of NVIDIA's RTX Voice. Since RTX Voice is closed source, this records files in real-time so should be used for experimental purposes and for library overhauls.

## Getting Started

**Requirements**

 - A Windows PC running NVIDIA RTX Voice (GTX GPU's work fine for this using this [guide](https://www.windowscentral.com/how-enable-rtx-voice-all-nvidia-gpus-including-older-geforce-gtx-cards)) [https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/](https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/)
 - VB Audio (Virtual Cable) [https://www.vb-audio.com/Voicemeeter/](https://www.vb-audio.com/Voicemeeter/)
 - Python 3.7


**Steps**

1 ) Clone the repository and cd into it

    git clone https://github.com/amirmaula/rtx-acapella.git

2 ) Install the prerequisites via

    pip install -r requirements.txt 

If you face issues installing PyAudio, the .whl files are included for Python 3.7 and can be installed using

    pip install wheel
    pip install ./PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
    
    ^ for 64 Bit installations of Python 3.7

3 ) Set RTX Voice's microphone input to your VB Audio Cable (Virtual AUX)

4 ) To execute the program, run it in your CLI like so:

    ./rtx-core.py -i [input path] -o [file directory & name for output]
   For example
   

    ./rtx-core.py -i song.flac -o D:\Music\Acapella\cool_song.wav


5 ) Follow the on screen prompts. 

6 ) Your new file will then be exported to code's directory. 


**To-do**

- ~~Add FLAC support~~ **DONE**
- ~~Create and load config file so that the user does not need to select input/output everytime~~ **DONE**
- Add GUI
- Add a real-time timer of how long a file has been playing for

**Known Issues**
- Sometimes the config file will get messed up so just delete the config.cfg
- The code will crash if the folder you wish to export your .wav to does not already exist, so just create the folder beforehand and it will save with no issues



Results may vary with this and you can tweak the noise suppression to what works for you. This can be used for songs and speech etc.


This is work in progress and I am somewhat an amateur when it comes to coding so any improvements made to the code and constructive criticism is greatly appreciated.


NVIDIA RTX is propriety software and belongs to NVIDIA and all rights are reserved. This program uses the NVIDIA RTX software as intended and does not use any exploitation.
