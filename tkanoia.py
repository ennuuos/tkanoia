from Tkinter import *
from Troubleshooter import Troubleshooter
from FTroubleshooter import FTroubleshooter
from Clearances import Clearances

class App:
    def __init__(self, master):

        self.initData()

        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

        FTroubleshooter(master, self.t)

        FTroubleshooter(master, self.t2)

    def initData(self):
        self.t = Troubleshooter()
        self.t.clearance = Clearances.Red
        self.t2 = Troubleshooter()
        self.t2.clearance = Clearances.Violet

root = Tk()
app = App(root)
root.mainloop()
