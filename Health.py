from Enum import Enum

class Health:
    def __init__(self):

        self.Status = ('Okay', 'SNAFU', 'Wounded', 'Maimed', 'Down', 'Killed', 'Vaporised')

        self.LHand = 0
        self.RHand = 0
        self.LArm = 0
        self.RArm = 0
        self.LLeg = 0
        self.RLeg = 0
        self.Loins = 0
        self.Misc = 0
