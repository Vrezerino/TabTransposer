import sys
import tkinter as tk
from tkinter import filedialog, Frame, Button, Text, messagebox as mb
import shutil

from PyQt5.QtWidgets import QApplication
import dialog

root = tk.Tk()
root.geometry('500x500')
root.title('Transpose notes in tab file')
#root.withdraw()

def copy_file():
    try:
        orig_filepath = filedialog.askopenfilename()
        name_and_extension = orig_filepath.split(".")
        #Append "_copy" to new file's name and attach extension.
        copy_filepath = name_and_extension[0] + '_copy.' + name_and_extension[1] 
        
        #to be continued
        return copy_filepath
    except IOError:
        print("IOError")

def handleFile(path):
    try:
        file = open(path, 'r')
        for line in file:
            print(line)
    except IOError:
        print("File not found or file corrupted.")

def preparation(path):
    app = QApplication(sys.argv)
    dlg = dialog.Dialog()
    dlg.show()

    if dlg.ok.isEnabled():
        print('go')
        handleFile(path)
        sys.exit(app.exec_())

path = copy_file()
preparation(path)