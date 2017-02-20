from Enum import Enum

class Health:
    Status = ('Okay', 'SNAFU', 'Wounded', 'Maimed', 'Down', 'Killed', 'Vaporised')
    BodyPart = ('LHand', 'RHand', 'LArm', 'RArm', 'LLeg', 'RLeg', 'Loins', 'Chest', 'Misc')
    def __init__(self):

        self.status = (0, 0, 0, 0, 0, 0, 0, 0, 0)

    def printStatus(self):
        for i, val in self.status:
            print(BodyPart(i) +':', Status(val))
