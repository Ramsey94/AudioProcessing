##############################################################
############ IMPORT LIBRARIES AND STUFF ######################
##############################################################

# TKINTER DEPENDENCIES #
import numpy as np


import tkinter as tk
from tkinter import Button
from tkinter import filedialog

# import the os module #
import os
from datetime import datetime

# Libreria para module finds all the pathnames matching a specified pattern 
from glob import glob


# Convert mp3 to wav using external software ffmpeg* ########
from pydub import AudioSegment

# Librosa stuff
import librosa
from librosa import load
from librosa.effects import trim


# Para escribir wav
from scipy.io.wavfile import write

# Para corregir un error random
#import sklearn
#from sklearn.metrics import classification_report
#from sklearn.metrics import _pairwise_distances_reduction

###############################################################3


root = tk.Tk()
# Define geometry of window
root.geometry("200x200") 
#Set title
root.title("AnalyzeIt!")
my_dir='Select folder'

# Definir funcion que tendr]a el boton
def myClick():
    
    myLabel = tk.Label(root, text="Data is being processed")
    myLabel.pack()
    my_dir = filedialog.askdirectory() # Carpeta de entrada
    myLabel.config(text=my_dir)
    label.config(text=my_dir)
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
        sound.export(PathFolder+folder+'/'+output_file, format="wav")

## DE AQUI para arriba todo well con pyinstaller

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




myButton = Button(root, text = "Load", command=myClick)
myButton.pack(padx=10, pady=40)


#Definir titulo, fuente y tama;o fuente
label = tk.Label(root, text=my_dir , font=('Arial', 12))
#Pading para el titulo label para darle espacio frente a las ventanas
label.pack(padx=50, pady=20)

root.mainloop()

