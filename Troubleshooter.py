from Skills import Skills
from Clearances import Clearances

class Troubleshooter:
    def __init__(self):

        self.name = "ERROR"
        self.clearance = Clearances.Infrared
        self.sector = "ERROR"
        self.clone = 1
        self.player = "ERROR"
        self.skills = Skills()


    def designation(self):
        return self.name + '-' + self.clearance.abbr + '-' + self.sector + '-' + str(self.clone)

class Equipment:
    def __init__(self):

        self.personal = None
        self.assigned = None
        self.treasonous = None
