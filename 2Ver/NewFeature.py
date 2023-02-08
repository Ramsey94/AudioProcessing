'''Notas:

 human speech falls within a frequency range of approximately 85-255 Hz 
 for male voices and 165-255 Hz for female voices. Additionally, the 
 frequency of human speech usually peaks between 100-150 Hz for males 
 and 200-250 Hz for females.


librosa.effects.split(y=buffer, frame_length=8000, top_db=40)
Split an audio signal into non-silent intervals.
Given sampling rate of 8000 it will split the audio by detecting audio lower than 40db for period of 1 sec

librosa.effects.split(y=buffer, frame_length=8000, top_db=40)

'''


# Libraries
################################################# IMPORT LIBRARIES FOR MAIN SCRIPT #########################################################
import sys
import pydub

# TKINTER DEPENDENCIES #
import numpy as np
import tkinter as tk
from tkinter import Button
from tkinter import filedialog

# import the os module #
import os
from datetime import datetime
from datetime import timedelta

# Libreria para module finds all the pathnames matching a specified pattern 
from glob import glob


# Convert mp3 to wav using external software ffmpeg* ########
from pydub import AudioSegment

# Librosa stuff
import librosa
from librosa import load
from librosa.effects import trim

# Para escribir wav
from scipy.io.wavfile import write, read

# Pandas for excel files working
import pandas as pd

# IMPORT LIBRARIES FOR GUI
from tkinter import *  # CHECK THIS LINE TO NOT IMPORT EVERYTHING FURTHER IN THE WAY


############### FEATURE STARTS HERE AND SHOULD BE ADD ON MAIN CODE ON LINE 161 ##########

# New Libraries

from scipy import signal




# Function to give time about spliting
def displayTime(startFrame, endFrame):    
    print(' start time: ' + str(startFrame/sr) + ', end time: ' + str(endFrame/sr))
# input file signal
input_file = '30SegSilence.mp3'
y, sr =librosa.load(input_file)
print(f'shape y: {y.shape}')
print(f'sr:{sr}')
## remove silences at begining and end
#y_trimmed, index =librosa.effects.trim(y, top_db=20)
# print(f'sample rate:{sr}') sample freq util for filtering
pass # test line

# Filter signal

# Sample rate (samples/second)
fs = sr

# Cutoff frequencies (Hz)
lowcut = 85
highcut = 255

# Create the filter coefficients
nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist
b, a = signal.butter(4, [low, high], btype='band')

# Generate a signal with some noise
t = np.linspace(0, 1, fs, endpoint=False)

# Apply the filter to the noisy signal
z = signal.filtfilt(b, a, y)
print(f'shape z: {z.shape}')


# Detect silences in signal to identify the 30sec ones
nonMuteSection = librosa.effects.split(z, top_db= 20,frame_length=22050)
nonMuteSection
for i in nonMuteSection:
    displayTime(i[0],i[1])

pass
