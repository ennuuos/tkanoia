from Clearance import Clearance

class Designation:
    def __init__(self):
        self.name = None
        self.clearance = clearance.infrared
        self.sector = None
        self.clone = 1

        self.designation = (str(self.name)+'-'+str(self.clearance.abbr)+'-'+str(self.sector)+'-'+str(self.clone))
