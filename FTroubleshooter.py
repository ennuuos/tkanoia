from Tkinter import *
from Health import Health

class FTroubleshooter:
    def __init__(self, master, troubleshooter):

        self.troubleshooter = troubleshooter

        self.frame = Frame(master, bg = self.troubleshooter.clearance.color)
        self.frame.pack(fill = BOTH, expand = 1, ipadx = 10, ipady=10, side=LEFT)

        self.l_designation = Label(self.frame, text = self.troubleshooter.designation())
        self.l_designation.pack(fill=X)

        self.l_player = Label(self.frame, text = troubleshooter.player)
        self.l_player.pack(fill=X)

        h=0
        for k, v in self.troubleshooter.health.status.iteritems():
            if v > h:
                h = v
        status = Health.Status[h]

        self.l_status = Label(self.frame, text = 'Status: Somewhat {0}'.format(status), fg=Health.StatusColor[h])
        self.l_status.pack(fill=X)

        self.b_health = Button(self.frame, text = "Medical Status", fg="green", command=self.troubleshooter.health.printStatus)
        self.b_health.pack(fill=X)
