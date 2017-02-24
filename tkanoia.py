from Tkinter import *
from Troubleshooter import Troubleshooter
from FTroubleshooter import FTroubleshooter
from Clearances import Clearances

class App:
    def __init__(self, master):

        self.initData()

        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

        self.f_troubleshooters = Frame(self.frame)
        self.f_troubleshooters.grid(row=0)
        self.f_content = Frame(self.frame)
        self.f_content.grid(row=1)

        self.inittesttrouble(self.f_troubleshooters)



    def inittesttrouble(self, master):

        self.troubleshooters = []

        self.t = Troubleshooter()
        self.t.clearance = Clearances.Infrared
        self.t.health.status['LHand'] = 6
        self.troubleshooters.append(self.t)

        self.t = Troubleshooter()
        self.t.clearance = Clearances.Red
        self.troubleshooters.append(self.t)

        self.t = Troubleshooter()
        self.t.clearance = Clearances.Orange
        self.troubleshooters.append(self.t)

        self.t = Troubleshooter()
        self.t.clearance = Clearances.Yellow
        self.troubleshooters.append(self.t)


        for i, troubleshooter in enumerate(self.troubleshooters):
            f = Frame(master, bg='red')
            f.grid(row=0, column=i)
            master.grid_columnconfigure(i, weight=1, uniform="troubleshooter")
            FTroubleshooter(f, troubleshooter, self.f_content)




    def initData(self):
        pass


root = Tk()
app = App(root)
root.mainloop()
