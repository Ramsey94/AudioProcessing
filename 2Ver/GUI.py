
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

################################################### INITIALIZE MAIN WINDOW #####################################################

root = Tk()
root.title("AnalyzeIt!")
root.iconbitmap('icon.ico') 
root.geometry("646x121")

################################################### CREATING WIDGETS ############################################################

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



################################################### CREATE BUTTON'S FUNCTIONS ###################################################

# Create fcn to Browse input
def BrowseIn():
    mylabel6 = Label(root, text='Folder is being loaded', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    root.filename = filedialog.askdirectory(title="Select Input Folder")
    global inputFolder
    inputFolder=root.filename
    myLabel4 = Label(root, text=root.filename, width=50, anchor="e", background='white').grid(row=0, column=1,
       columnspan = 2)
    mylabel6 = Label(root, text='Input Folder Selected!', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    myButton2 = Button(root, text="ANALYSE", pady=3,state=NORMAL, padx=60, command=Analyze)
    myButton2.grid(row=3, column=1, padx=1, pady=1)
    return inputFolder

# Create fcn to Browse output
def BrowseOut():
    mylabel6 = Label(root, text='Folder is being loaded', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    root.filename = filedialog.askdirectory(title="Select Output Folder")
    global outputFolder
    outputFolder=root.filename
    myLabel5 = Label(root, text=root.filename, width=50, anchor="e", background='white').grid(row=1, column=1,
       columnspan = 2)
    mylabel6 = Label(root, text='Output Folder Selected!', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)
    
    return outputFolder

# Create fcn to Browse output
def Analyze():
    myButton4 = Button(root, text="EXPORT", pady=3,state=NORMAL, padx=60, command=Export)
    myButton4.grid(row=3, column=2, padx=1, pady=1)
    # Create directory for the output files
    from datetime import datetime
    now = datetime.now()
    # dd-mm-aaaa-hms
    dt_string = now.strftime(r"%d-%m-%Y-%H%M%S")
    # detect the output directory
    path = outputFolder
    PathFolder=path+"/"
    global folder
    folder = dt_string

    try:
        os.mkdir(PathFolder+folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        
        print ("Successfully created the directory %s " % folder)

    mylabel6 = Label(root, text="Successfully created the directory %s " % folder, width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)

    mylabel6 = Label(root, text='Folder Analyzed Succesfully!', width=50, anchor="center", background='white').grid(row=2, column=1,
       columnspan = 2)


    input_file = glob(inputFolder+'/'+'*.mp3') #Folder Path of recordings
    for i in input_file: # Reading each file in folder with extension mp3
        #print(i)
        my_string=i
        my_string2=my_string.split("\\",1)[1]
        my_string3=my_string2.split(".",1)[0]
        #print(my_string3) # Print the name of original file

        # assign files
        input_file = i
        output_file = my_string3+'.wav'

        # convert mp3 file to wav file ##########################################################

        sound = AudioSegment.from_mp3(i)
        sound.export(PathFolder+folder+'/'+output_file, format="wav")

    print ("Audios convertidos a WAV con exito!")
    input_file = glob(PathFolder+folder+'/'+'*.wav') #Folder Path of recordings

    k=0       

    for i in input_file: # Reading each file in folder with extension mp3
        y, sr =librosa.load(i)
        y_trimmed, index =librosa.effects.trim(y, top_db=20)
        my_string=i
        my_string2=my_string.split("\\",1)[1]
        my_string3=my_string2.split(".",1)[0]
            # assign files
        input_file = i
        output_file = my_string3+'-T.wav'

        write(PathFolder+folder+'/'+output_file,sr, y_trimmed)
        os.remove(PathFolder+folder+'/'+my_string3+'.wav')

#########33  hasta aqui todo ok

        print("Start Summary processing")
        ## READING TIME
        reading_time = index[1]/sr-index[0]/sr
        # SAVED TIME FOR LISTENER
        listening_time_saved = ((y.shape[0]-1)/sr)- reading_time  
        ## Start reading timestamp
        startFrame = index[0]/sr
        # End reading timestamp
        endFrame = index[1]/sr
        ## Recording file name
        recFileName = my_string3+'.mp3'

        import datetime

        # Convert seconds to hh:mm:ss
        startFrame = str(datetime.timedelta(seconds=round(startFrame,2)) )
        startFrame = startFrame[0:10]
        
        endFrame = str(datetime.timedelta(seconds=round(endFrame,2)) )
        endFrame = endFrame[0:10]


        # Create the dataframe on the fist bucle
        if k==0 :
            data = [[recFileName, round(reading_time,2), startFrame, endFrame, round(listening_time_saved,2)]]
            # Create the pandas DataFrame
            global df
            df = pd.DataFrame(data, columns=['Recording Filename', 'reading time (s)', 'start reading', "end reading","time saved (s)"])
            #Nota: Se deben corregir los formatos de las variables para que sea mas entendible todo
            k=k+1
        else :
            new_row = {'Recording Filename':recFileName, 'reading time (s)':round(reading_time,2), 'start reading':startFrame, 'end reading':endFrame, 'time saved (s)':round(listening_time_saved,2)}
            
            df = df.append(new_row, ignore_index=True)

# Create fcn to Export
def Export():
           #  Excel file creation
        out_path = outputFolder+'/'+folder+'/'+'Summary.xlsx'
        writer = pd.ExcelWriter(out_path)

    # write dataframe to excel

        df.to_excel(writer, sheet_name='Sheet1')


    # save the excel
        writer.save()
        print("DataFrame is exported successfully to 'Summary.xlsx' Excel File.")
        mylabel6 = Label(root, text="Files successfully exported to directory ", width=50, anchor="center", background='white').grid(row=2, column=1,
        columnspan = 2)

# Define myButtons
myButton1 = Button(root, text="EXIT", pady=3, padx=60, command=root.destroy, fg="white", bg="blue").grid(row=3, column=0, padx=1, pady=1) #padx: anchura
myButton2 = Button(root, text="ANALYSE", pady=3,state=DISABLED, padx=60, command=Analyze).grid(row=3, column=1, padx=1, pady=1) #padx: anchura
myButton4 = Button(root, text="EXPORT", pady=3,state=DISABLED, padx=60, command=Export).grid(row=3, column=2, padx=1, pady=1) #padx: anchura
myButton5 = Button(root, text="BROWSE", pady=3, padx=40, command=BrowseIn).grid(row=0, column=3, padx=1, pady=1) #padx: anchura
myButton6 = Button(root, text="BROWSE",  pady=3, padx=40, command=BrowseOut).grid(row=1, column=3, padx=1, pady=1) #padx: anchura


root.mainloop()

