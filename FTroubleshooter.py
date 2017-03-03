from Tkinter import *
from Health import Health

class FTroubleshooter:
    def __init__(self, master, troubleshooter, f_content):

        self.troubleshooter = troubleshooter
        self.f_content = f_content

        self.frame = Frame(master, bg = self.troubleshooter.clearance.color, bd=10)
        self.frame.pack(fill = BOTH, expand = 1)

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

        self.b_more = Button(self.frame, text = "More", command = self.openDetails)
        self.b_more.pack(fill=X)


    def openDetails(self):
        for child in self.f_content.winfo_children():
            child.destroy()

        FTroubleshooterDetails(self.f_content, self.troubleshooter)


class FTroubleshooterDetails:
    def __init__(self, master, troubleshooter):
        self.frame = Frame(master)
        self.frame.pack(fill=BOTH, expand=1)
        self.troubleshooter = troubleshooter

        self.l_designation = Label(self.frame, text = self.troubleshooter.designation(), pady = 15)
        self.l_designation.pack()

        self.f_skills = LabelFrame(master, text="Skills", padx=5, pady=5)
        self.f_skills.pack(fill=X, expand = 1)
        FTroubleshooterSkills(self.f_skills, self.troubleshooter)


        self.f_inventory = LabelFrame(master, text="Inventory", padx=5, pady=5)
        self.f_inventory.pack(side=LEFT, fill = Y, expand = 1)
        FTroubleshooterInventory(self.f_inventory, self.troubleshooter)

        self.f_medical = LabelFrame(master, text="Medical Status", padx=5, pady=5)
        self.f_medical.pack(side=LEFT, fill = Y, expand = 1)
        FTroubleshooterMedical(self.f_medical, self.troubleshooter)

class FTroubleshooterSkills:
    def __init__(self, master, troubleshooter):
        for group in troubleshooter.skills.groups:
            gFrame = LabelFrame(master, text = group.name, pady = 15, padx=5)
            gFrame.pack(fill=X)
            for t in group.types:
                tFrame = LabelFrame(gFrame, text = "{0} - {1}".format(t.name, t.level), pady = 15, padx=5)
                tFrame.pack(side = LEFT, fill=Y, expand = 1)
                tModFrame = Frame(tFrame)
                tModFrame.pack(fill=X)
                bLowerT = Button(tModFrame, text="-")
                bLowerT.grid(row=0, column = 0)
                bUpperT = Button(tModFrame, text="+")
                bUpperT.grid(row=0, column = 1)
                for skill in t.skills:
                    sLabel = Label(tFrame, text = "{0} - {1}".format(skill.name, skill.level))
                    sLabel.pack(fill=X)


class FTroubleshooterInventory:
    def __init__(self, master, troubleshooter):
        self.f_personal = LabelFrame(master, text="Personal", padx=5, pady=5)
        self.f_personal.pack(side=LEFT, fill = Y, expand = 1)
        for i in range(6):
            self.l_item = Label(self.f_personal, text = "{0} - {1}".format("Item", "State"))
            self.l_item.pack(fill=X)

        self.f_Assigned = LabelFrame(master, text="Assigned", padx=5, pady=5)
        self.f_Assigned.pack(side=LEFT, fill = Y, expand = 1)
        for i in range(5):
            self.l_item = Label(self.f_Assigned, text = "{0} - {1}".format("Item", "State"))
            self.l_item.pack(fill=X)

        self.f_Treasonous = LabelFrame(master, text="Treasonous", padx=5, pady=5)
        self.f_Treasonous.pack(side=LEFT, fill = Y, expand = 1)
        for i in range(15):
            self.l_item = Label(self.f_Treasonous, text = "{0} - {1}".format("Item", "State"))
            self.l_item.pack(fill=X)

class FTroubleshooterMedical:
    def __init__(self, master, troubleshooter):

        for k, v in troubleshooter.health.status.iteritems():
            self.l_stat = Label(master, text = '{0}: {1}'.format(k, Health.Status[v]), fg=Health.StatusColor[v])
            self.l_stat.pack(fill=X)
