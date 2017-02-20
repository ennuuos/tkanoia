from Enum import Enum

class Health:
    Status = ('Okay', 'SNAFU', 'Wounded', 'Maimed', 'Down', 'Killed', 'Vaporised')
    def __init__(self):


        self.status = {
            LHand : 0,
            RHand : 0,
            LArm : 0,
            RArm : 0,
            LLeg : 0,
            RLeg : 0,
            Loins : 0,
            Misc : 0

        }

        print Status(self.status.LHand)

    def printStatus(self):
        pass
