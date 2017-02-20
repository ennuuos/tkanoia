from Skills import Skills
from Clearances import Clearances
from Health import Health

class Troubleshooter:
    def __init__(self):

        self.name = "ERROR"
        self.clearance = Clearances.Infrared
        self.sector = "ERROR"
        self.clone = 1
        self.player = "ERROR"
        self.skills = Skills()
        self.health = Health()


    def designation(self):
        return '{0}-{1}-{2}-{3}'.format(self.name, self.clearance.abbr, self.sector, str(self.clone))
