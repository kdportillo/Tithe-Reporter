from tkinter import Label, Button, Checkbutton, IntVar, filedialog, messagebox
from pandas import read_csv
import os


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Tithe Reporter")
        master.geometry('1000x500')

        self.filepath = ""
        self.cmd = 0
        self.names = []

        self.label = Label(master, text="File Search")
        self.label.pack()

        self.file_button = Button(master, text="Choose a file", command=self.filesearch)
        self.file_button.pack()

        self.makeboxes_button = Button(master, text="Retrieve Names", command=self.makeboxes)
        self.makeboxes_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def filesearch(self):
        tmpdir = filedialog.askopenfilename(initialdir=os.getcwd(), title='Choose file')
        if tmpdir:
            try:
                self.file_button.configure(text='File Found', bg='green')
                self.filepath = tmpdir
                self.getnames()
            except:
                messagebox.showerror("Open source file", "Failed to read file" + tmpdir)

    def getnames(self):
        df = read_csv(self.filepath, encoding='utf-8')
        self.names = df['Name'].tolist()

    def makeboxes(self):
        try:
            for name in self.names:
                var = IntVar()
                self.check_buttons = Checkbutton(self.master, variable=var, text=name)
                self.check_buttons.pack()
        except:
            messagebox.showerror("Populate Names", "Failed to create list of names")
