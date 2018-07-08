import sys
from tkinter import Tk
sys.path.insert(0, '../lib/')
import gui

if __name__ == '__main__':
    root = Tk()
    window = gui.GUI(root)
    root.mainloop()

