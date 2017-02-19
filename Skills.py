

class Skills:
    @classmethod
    def __init__(self):

        self.action = Skills.Action()
        self.knowledge = Skills.Knowledge()
        self.secret = Skills.Secret()

    class Action:
        def __init__(self):

            self.management = Skills.Action.Management()
            self.stealth = Skills.Action.Stealth()
            self.violence = Skills.Action.Violence()



        class Management:
            def __init__(self):

                self.bootlicking = 7
                self.chutzpah = 7
                self.congames = 7
                self.hygiene = 7
                self.interrogation = 7
                self.moxie = 7
                self.oratory = 7

        class Stealth:
            def __init__(self):

                self.concealment = 7
                self.disguise = 7
                self.highalert = 7
                self.securitysystems = 7
                self.shadowing = 7
                self.sleight = 7
                self.surveilance = 7

        class Violence:
            def __init__(self):

                self.agility = 7
                self.energy = 7
                self.field = 7
                self.fine = 7
                self.hand = 7
                self.projectie = 7
                self.thrown = 7
                self.unarmed = 7
                self.vehicular = 7

    class Knowledge:
        def __init__(self):

            self.hardware = Skills.Knowledge.Hardware()
            self.software = Skills.Knowledge.Software()
            self.wetware = Skills.Knowledge.Wetware()

        class Hardware:
            def __init__(self):

                self.bot = 7
                self.chemical = 7
                self.electronic = 7
                self.habitat = 7
                self.mechanical = 7
                self.nuclear = 7
                self.vehicle = 7
                self.weapon = 7

        class Software:
            def __init__(self):

                self.bot = 7
                self.c = 7
                self.dataA = 7
                self.dataS = 7
                self.financial = 7
                self.hacking = 7
                self.operating = 7
                self.vehicle = 7

        class Wetware:
            def __init__(self):

                self.bioS = 7
                self.bioW = 7
                self.cloning = 7
                self.medical = 7
                self.oudoor = 7
                self.pharmatherapy = 7
                self.Psychtherapy = 7
                self.suggestion = 7

    class Secret:
        def __init__(self):
            self.uncommon = Skills.Secret.Uncommon()
            self.unlikely = Skills.Secret.Unlikely()
            self.unhealthy = Skills.Secret.Unhealthy()

        class Uncommon:
            pass


        class Unlikely:
            pass


        class Unhealthy:
            pass
