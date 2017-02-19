from Tkinter import *
from Troubleshooter import Troubleshooter
from FTroubleshooter import FTroubleshooter
from Clearance import Clearance

class App:
    def __init__(self, master):

        self.initData()

        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

        FTroubleshooter(master, self.t)

    def initData(self):
        self.t = Troubleshooter()

root = Tk()
app = App(root)
root.mainloop()
