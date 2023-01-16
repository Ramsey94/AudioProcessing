
############ IMPORT LIBRARIES FOR MAIN SCRIPT ######################


import sys
import pydub

########################3

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

############ IMPORT LIBRARIES FOR GUI ######################

from tkinter import *  # CHECK THIS LINE TO NOT IMPORT EVERYTHING FURTHER IN THE WAY
from tkinter import filedialog


############ INITIALIZE MAIN WINDOW ######################

root = Tk()
root.title("AnalyseIt!")
root.iconbitmap('icon.ico') 
root.geometry("646x121")

############ CREATING WIDGETS ######################

# Creating a label widget
myLabel1 = Label(root, text='Input File')
myLabel2 = Label(root, text='Output File')
myLabel3 = Label(root, text='Status')
# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

# Creating a label widget
myLabel1 = Label(root, text='Input File', pady=3)
myLabel2 = Label(root, text='Output File', pady=3)             
myLabel3 = Label(root, text='Status', pady=3)
# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

# Create blank spaces for paths and status
mylabel4 = Label(root, text='', width=50, anchor="e", background='white').grid(row=0, column=1,
       columnspan = 2)
mylabel5 = Label(root, text='', width=50, anchor="e", background='white').grid(row=1, column=1,
       columnspan = 2)
mylabel6 = Label(root, text='Please select input and output folder', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)


# Create fcn to Browse input
def myClick1():
    mylabel6 = Label(root, text='Folder is being loaded', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    root.filename = filedialog.askdirectory(title="Select Input Folder")
    myLabel4 = Label(root, text=root.filename, width=50, anchor="e", background='white').grid(row=0, column=1,
       columnspan = 2)
    mylabel6 = Label(root, text='Input Folder Selected!', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    myButton2 = Button(root, text="ANALYSE", pady=3,state=NORMAL, padx=60, command=Analyze)
    myButton2.grid(row=3, column=1, padx=1, pady=1)

# Create fcn to Browse output
def myClick2():
    mylabel6 = Label(root, text='Folder is being loaded', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    root.filename = filedialog.askdirectory(title="Select Output Folder")
    myLabel5 = Label(root, text=root.filename, width=50, anchor="e", background='white').grid(row=1, column=1,
       columnspan = 2)
    mylabel6 = Label(root, text='Output Folder Selected!', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    myButton3 = Button(root, text="DISPLAY SUMMARY",  pady=3,state=NORMAL, padx=30, command=myClick1)
    myButton3.grid(row=3, column=2, padx=1, pady=1)

# Create fcn to Browse output
def Analyze():
    mylabel6 = Label(root, text='Folder is being Analyzed', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    myButton4 = Button(root, text="EXPORT", pady=3,state=NORMAL, padx=40, command=myClick1)
    myButton4.grid(row=3, column=3, padx=1, pady=1)
    print("Test line")



    

    

# Define myButtons
myButton1 = Button(root, text="EXIT", pady=3, padx=60, command=root.destroy, fg="white", bg="blue") #padx: anchura
myButton2 = Button(root, text="ANALYSE", pady=3,state=DISABLED, padx=60, command=Analyze) #padx: anchura
myButton3 = Button(root, text="DISPLAY SUMMARY",  pady=3,state=DISABLED, padx=30, command=myClick1) #padx: anchura
myButton4 = Button(root, text="EXPORT", pady=3,state=DISABLED, padx=40, command=myClick1) #padx: anchura

myButton5 = Button(root, text="BROWSE", pady=3, padx=40, command=myClick1) #padx: anchura
myButton6 = Button(root, text="BROWSE",  pady=3, padx=40, command=myClick2) #padx: anchura


myButton1.grid(row=3, column=0, padx=1, pady=1)
myButton2.grid(row=3, column=1, padx=1, pady=1)
myButton3.grid(row=3, column=2, padx=1, pady=1)
myButton4.grid(row=3, column=3, padx=1, pady=1)

myButton5.grid(row=0, column=3, padx=1, pady=1)
myButton6.grid(row=1, column=3, padx=1, pady=1)





root.mainloop()

