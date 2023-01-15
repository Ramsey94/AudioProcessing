from tkinter import * 
from tkinter import filedialog


root = Tk()
root.title("AnalyseIt!")
root.iconbitmap('icon.ico') 
root.geometry("646x121")


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


# Create fcn to myButton1
def myClick():
    root.filename = filedialog.askopenfilename(title="Select Folder")
    mylabel3 = Label(root, text=root.filename, width=50, anchor="e", background='white').grid(row=2, column=1,
       columnspan = 3)
    

# Define myButtons
myButton1 = Button(root, text="EXIT", pady=3, padx=60, command=root.destroy, fg="white", bg="blue") #padx: anchura
myButton2 = Button(root, text="ANALYSE", pady=3,state=DISABLED, padx=60, command=myClick) #padx: anchura
myButton3 = Button(root, text="DISPLAY SUMMARY",  pady=3,state=DISABLED, padx=30, command=myClick) #padx: anchura
myButton4 = Button(root, text="EXPORT", pady=3,state=DISABLED, padx=40, command=myClick) #padx: anchura

myButton5 = Button(root, text="BROWSE", pady=3,state=DISABLED, padx=40, command=myClick) #padx: anchura
myButton6 = Button(root, text="BROWSE",  pady=3,state=DISABLED, padx=40, command=myClick) #padx: anchura


myButton1.grid(row=3, column=0, padx=1, pady=1)
myButton2.grid(row=3, column=1, padx=1, pady=1)
myButton3.grid(row=3, column=2, padx=1, pady=1)
myButton4.grid(row=3, column=3, padx=1, pady=1)

myButton5.grid(row=0, column=3, padx=1, pady=1)
myButton6.grid(row=1, column=3, padx=1, pady=1)





root.mainloop()

