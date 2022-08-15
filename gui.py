from tkinter import *
from tkinter import Toplevel
from tkinter import ttk, filedialog as fd
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import filedialog
import os
import sys
from pathlib import Path
from script import script
# from turn_off_quick_edit import simple_off
# from upload import upload_data

#Main app class inherits from tk 
class main:
    #init function
    def __init__(self, master):
        self.master = master
        #Sets title of app window
        #simple_off()
        master.title("Get Webinar Information")
        

        self.fontStyle = tkFont.Font(family="Arial", size=12)
        self.fontStyle2 = tkFont.Font(family="Arial", size=7)
        self.fontStyle3 = tkFont.Font(family="Arial", size=10)

        #GUI elements
        self.dir_path = tk.StringVar()

        self.label = ttk.Label(master, text = '', font=self.fontStyle3).pack()
        self.cmo_button= ttk.Button(master, text = 'Get Data Directly From MyCMO and Run', command = lambda: self.open_cmo(master)).pack()
        self.label1 = ttk.Label(master, text = '', font=self.fontStyle3).pack()
        self.label2 = ttk.Label(master, text = '', font=self.fontStyle3).pack()
        self.file_button= ttk.Button(master, text = 'Get Data From File and Run', command = lambda: self.open_file(master)).pack()
        self.label3 = ttk.Label(master, text = '', font=self.fontStyle3).pack()
        self.filepathText = ttk.Label(master, textvariable = self.dir_path).pack()
       
    #Get file path
    def open_cmo(self, master):
        setup()
        tk.messagebox.showinfo(title='Complete', message='Check output folder')
    #Did this so next button would appear after file was selected
    def open_file(self, master):
        filename = fd.askopenfilename()
        self.dir_path.set(filename)
        file_setup(filename)
        


    def restart_program(self):
        self.python = sys.executable
        os.execl(self.python, self.python, * sys.argv)
        

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500")
    my_gui = main(root)
    root.mainloop()