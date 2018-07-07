from Tkinter import Tk, Label, Button, Text, DISABLED, Message
import tkFileDialog as fd
import os

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Tithe Reporter")
        master.geometry('1000x500')

        self.label = Label(master, text="File Search")
        self.label.pack()

        self.greet_button = Button(master, text="Choose a file", command=self.filesearch)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def filesearch(self):
        tmpdir = fd.askopenfilename(initialdir=os.getcwd(), title='Choose file')
        if len(tmpdir) > 0:
            return True
        else:
            return False