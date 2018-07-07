import sys
from Tkinter import Tk
sys.path.insert(0, '../lib/')
import gui

root = Tk()
window = gui.GUI(root)
root.mainloop()

