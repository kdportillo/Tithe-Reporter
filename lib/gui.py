from Tkinter import Tk, Label, Button, Text, DISABLED
import tkFileDialog as fd
import tkMessageBox as mb
import os

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Tithe Reporter")
        master.geometry('1000x500')

        self.fileFound = False

        self.label = Label(master, text="File Search")
        self.label.pack()

        self.file_button = Button(master, text="Choose a file", command=self.filesearch)
        self.file_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def filesearch(self):
        tmpdir = fd.askopenfilename(initialdir=os.getcwd(), title='Choose file')
        rtn = False
        if tmpdir:
            try:
                self.file_button.configure(text='File Found', bg='green')
            except:
                mb.showerror("Open source file", "Failed to read file" + tmpdir)