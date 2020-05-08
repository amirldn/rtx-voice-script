
# rtx_acapella
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![HitCount](http://hits.dwyl.com/amirmaula/rtx-acapella.svg)](http://hits.dwyl.com/amirmaula/rtx-acapella)



A python script that takes an input MP3 file and outputs an acapella version as a WAV using the power of NVIDIA's RTX Voice. Since RTX Voice is closed source, this records files in real-time so should be used for experimental purposes and for library overhauls.

## Getting Started

**Requirements**

 - A Windows PC running NVIDIA RTX Voice (GTX GPU's work fine for this) [https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/](https://www.nvidia.com/en-us/geforce/guides/nvidia-rtx-voice-setup-guide/)
 - Support for Stereo Mix or just install VB Audio (Virtual Cable) [https://www.vb-audio.com/Voicemeeter/](https://www.vb-audio.com/Voicemeeter/)
 - Python 3.8


**Steps**
1 ) Clone the repository and cd into it

    git clone https://github.com/amirmaula/rtx-acapella.git

2 ) Install the prerequisites via

    pip install -r requirements.txt 

You will need to be running Python 3.8, 32bit for this requirements.txt to work, else just pip install these dependencies manually:

    easygui==0.98.1  
    mutagen==1.44.0  
    PyAudio==0.2.11
    pygame==2.0.0.dev8

3 ) Set RTX Voice's microphone input to your Stereo Mix / VB Audio Cable
4 ) To execute the program, run it in your CLI like so:

    ./rtx-core.py -i [file input path] -o [file name for output]
   For example
   

    ./rtx-core.py -i ./Users/user/Downloads/cool_song.mp3 -o new_song


Your new file will then be exported to the git cloned directory. 

Results may vary with this and you can tweak the noise supression to what works for you. This can be used for songs and speech etc.



This is work in progress and I am somewhat an amateur when it comes to coding so any improvements made to the code and constructive criticism is greatly appreciated.

NVIDIA RTX is propriety software and belongs to NVIDIA and all rights are reserved. This program uses the NVIDIA RTX software as intended and does not use any exploitation.
