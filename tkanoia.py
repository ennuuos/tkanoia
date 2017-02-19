from Tkinter import *
from Troubleshooter import Troubleshooter
from FTroubleshooter import FTroubleshooter
from Clearance import Clearance

class App:
    def __init__(self, master):

        self.initData()

        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

        t = Troubleshooter()

        FTroubleshooter(master, t)


        c = Clearances.Infrared.promote()

        print c.color

    def initData(self):
        # self.troubleshooters = [
        #     Troubleshooter(),
        #     Troubleshooter()
        # ]
        # self.troubleshooters[0].name = "CA"
        # self.troubleshooters[0].clearance = 1
        pass

root = Tk()
app = App(root)
root.mainloop()
