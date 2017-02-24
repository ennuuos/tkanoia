from Tkinter import *

from collections import OrderedDict

class Health:
    Status = ('Okay', 'Snafu', 'Wounded', 'Maimed', 'Down', 'Killed', 'Vaporised')
    StatusColor = ('#3A0', '#5A0', '#780', '#960', '#b40', '#f00', '#000')
    def __init__(self):

        self.status = OrderedDict([
            ('LHand', 0),
            ('RHand', 0),
            ('LArm', 0),
            ('RArm', 0),
            ('LLeg', 0),
            ('RLeg', 0),
            ('Loins', 0),
            ('Chest', 0),
            ('Misc', 0)
        ]);
