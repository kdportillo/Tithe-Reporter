from Tkinter import Label, Button

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Tithe Reporter")

        self.label = Label(master, text="LABEL 1")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        def greet(self):
            print("Greetings")
