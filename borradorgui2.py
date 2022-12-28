##############################################################
############ IMPORT LIBRARIES AND STUFF ######################
##############################################################

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display  
import IPython.display as ipd

from itertools import cycle

sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])


# Mover archivos en carpetas
import shutil

# import the os module
import os
from datetime import datetime


# Para escribir wav
from IPython.display import Audio
from scipy.io.wavfile import read, write


# Convert mp3 to wav using external software ffmpeg* ########
from os import path
from pydub import AudioSegment
import ffmpeg
import sys


# library for handling time format



sys.path.append(r'C:\ffmpeg-5.1.2-full_build\bin')# PAth of local variables on local computer (MINE)

from tkinter import *
from tkinter import filedialog

root = Tk()


# Definir funcion que tendr]a el boton
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()
    my_dir = filedialog.askdirectory() # Carpeta de entrada
    myLabel.config(text=my_dir)
    ##############################################################
    ########## creating directories and receive path #############
    ##############################################################

    PathFolder=my_dir+"/" #### ***** #### ***** #### ***** ###

    ## Creating folder to receive the files processed 


    from datetime import datetime
    #and the access its now method simpler
    # datetime object containing current date and time
    now = datetime.now()
    

    # dd-mm-aaaa-hms
    dt_string = now.strftime("%d-%m-%Y-%H%M%S")


    # detect the current working directory and print it
    path = os.getcwd()



    folder = dt_string

    try:
        os.mkdir(PathFolder+folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s " % folder)



    import datetime


    ##############################################################
    ########## convert folder to mp3 using ffmpeg ################
    ##############################################################

    input_file = glob(PathFolder+'*.mp3') #Folder Path of recordings

    for i in input_file: # Reading each file in folder with extension mp3
        #print(i)
        my_string=i
        my_string2=my_string.split("\\",1)[1]
        my_string3=my_string2.split(".",1)[0]
        #print(my_string3) # Print the name of original file

        # assign files
        input_file = i
        output_file = my_string3+'.wav'

        # convert mp3 file to wav file
        sound = AudioSegment.from_mp3(i)
        sound.export(output_file, format="wav")

    #####################################################################
    ######################## TRIMMING SIGNALS ###########################
    #####################################################################

    def displayTime(startFrame, endFrame):    # Function to convert sample number to time
        print('Start reading: ' + str(round(startFrame/sr,2)) +' s' + ', end reading: ' + str(round(endFrame/sr,2)) + ' s')


    input_file = glob(PathFolder+'*.wav') #Folder Path of recordings

    k=0 

    for i in input_file: # Reading each file in folder with extension mp3


        #print(i)
        y, sr =librosa.load(i)
        y_trimmed, index =librosa.effects.trim(y, top_db=20)
        my_string=i
        my_string2=my_string.split("\\",1)[1]
        my_string3=my_string2.split(".",1)[0]
        #print(my_string3) # Print the name of original file

        # assign files
        input_file = i
        output_file = my_string3+'-T.wav'

        write(output_file,sr, y_trimmed)
        old_path=path+'\\'+my_string3+'-T.wav'
        new_path=path+'\\'+folder+'\\'+my_string3+'-T.wav'
        shutil.move(old_path, new_path )
        ########  Remove temporal files
        os.remove(my_string3+'.wav')

        ############### Summary of recording #######################################

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

        # Convert seconds to hh:mm:ss
        startFrame = str(datetime.timedelta(seconds=round(startFrame,2)) )
        startFrame = startFrame[0:10]
        
        endFrame = str(datetime.timedelta(seconds=round(endFrame,2)) )
        endFrame = endFrame[0:10]


        # Create the dataframe on the fist bucle
        if k==0 :
            data = [[recFileName, round(reading_time,2), startFrame, endFrame, round(listening_time_saved,2)]]
            # Create the pandas DataFrame
            df = pd.DataFrame(data, columns=['Recording Filename', 'reading time (s)', 'start reading', "end reading","time saved (s)"])
            #Nota: Se deben corregir los formatos de las variables para que sea mas entendible todo
            k=k+1
        else :
            new_row = {'Recording Filename':recFileName, 'reading time (s)':round(reading_time,2), 'start reading':startFrame, 'end reading':endFrame, 'time saved (s)':round(listening_time_saved,2)}
            df = df.append(new_row, ignore_index=True)

    df


    ##############################################################
    ################## creating excel file #######################
    ##############################################################

    out_path = path+'\\'+folder+'\\'+'Summary.xlsx'
    writer = pd.ExcelWriter(out_path)

    # write dataframe to excel

    df.to_excel(writer, sheet_name='Sheet1')


    # save the excel
    writer.save()
    print("DataFrame is exported successfully to 'Summary.xlsx' Excel File.")








myButton = Button(root, text = "Click Me!", command=myClick)
myButton.pack()

root.mainloop()
