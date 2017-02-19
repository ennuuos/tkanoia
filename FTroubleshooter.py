

class FTroubleshooter:
    def __init__(self, master, troubleshooter):

        self.troubleshooter = troubleshooter

        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

        self.l_designation = Label(self.frame, troubleshooter.designation())
        self.l_designation.pack(fill=X)

        self.l_player = Label(self.frame, troubleshooter.player)
        self.l_player.pack(fill=X)

        self.b_health = Button(self.frame, text = "Medical Status", fg="green")
        self.b_health.pack(fill=X)
