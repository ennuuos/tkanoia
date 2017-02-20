from Tkinter import *

from collections import OrderedDict

class Health:
    Status = ('Okay', 'Snafu', 'Wounded', 'Maimed', 'Down', 'Killed', 'Vaporised')
    StatusColor = ('#3C2', '#5A0', '#780', '#960', '#b40', '#f00', '#000')
    def __init__(self):

        self.status = OrderedDict([
            ('LHand', 0),
            ('RHand', 1),
            ('LArm', 2),
            ('RArm', 3),
            ('LLeg', 3),
            ('RLeg', 3),
            ('Loins', 3),
            ('Chest', 0),
            ('Misc', 0)
        ]);


    def printStatus(self):

        self.top = Toplevel()
        self.top.title('Medical Status')

        for k, v in self.status.iteritems():
            self.l_stat = Label(self.top, text = '{0}: {1}'.format(k, Health.Status[v]), fg=Health.StatusColor[v])
            self.l_stat.pack(fill=X)

        self.b_dismiss = Button(self.top, text="Dismiss", command=self.top.destroy, fg = 'green')
        self.b_dismiss.pack(fill=X)
