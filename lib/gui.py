from Tkinter import Label, Button
import tkFileDialog as fd
import tkMessageBox as mb
import os

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Tithe Reporter")
        master.geometry('1000x500')

        self.filepath = ""

        self.label = Label(master, text="File Search")
        self.label.pack()

        self.file_button = Button(master, text="Choose a file", command=self.filesearch)
        self.file_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def filesearch(self):
        tmpdir = fd.askopenfilename(initialdir=os.getcwd(), title='Choose file')
        if tmpdir:
            try:
                self.file_button.configure(text='File Found', bg='green')
                self.filepath = tmpdir
                print(tmpdir, type(tmpdir))
            except:
                mb.showerror("Open source file", "Failed to read file" + tmpdir)