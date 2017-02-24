

class Skills:
    def __init__(self):
        self.groups = []

        g = self.addGroup("Action")
        t = g.addType("Management", 7)
        t.addSkill("Bootlicking")
        t.addSkill("Chutzpah")
        t.addSkill("Con Games")
        t.addSkill("Hygeine")
        t.addSkill("Interrogation")
        t.addSkill("Intimidation")
        t.addSkill("Moxie")
        t.addSkill("Oratory")


        t = g.addType("Stealth", 7)
        t.addSkill("Concealment")
        t.addSkill("Disguise")
        t.addSkill("High Alert")
        t.addSkill("Security Systems")
        t.addSkill("Shadowing")
        t.addSkill("Sleight of Hand")
        t.addSkill("Sneaking")
        t.addSkill("Surveillance")

        t = g.addType("Violence", 7)
        t.addSkill("Agility")
        t.addSkill("Energy Weapons")
        t.addSkill("Demolition")
        t.addSkill("Field Weapons")
        t.addSkill("Fine Manipulation")
        t.addSkill("Hand Weapons")
        t.addSkill("Projectile Weapons")
        t.addSkill("Thrown Weapons")
        t.addSkill("Unarmed Combat")
        t.addSkill("Vehicular Combat")

        g = self.addGroup("Knowledge")
        t = g.addType("Hardware", 7)
        t.addSkill("Bot Ops & Maintenance")
        t.addSkill("Chemical Engineering")
        t.addSkill("Electronic Engineering")
        t.addSkill("Habitat Engineering")
        t.addSkill("Mechanical Engineering")
        t.addSkill("Nuclear Engineering")
        t.addSkill("Vehicle Ops & Maintenance")
        t.addSkill("Weapon & Armor Maintenance")

        g = self.addGroup("Secret")

    def addGroup(self, name):
        self.groups.append(Group(name))
        return self.groups[-1]

class Group:
    def __init__(self, name):
        self.name = name
        self.types = []

    def addType(self, name, level):
        self.types.append(Type(name, level))
        return self.types[-1]

class Type:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.skills = []

    def addSkill(self, name):
        self.skills.append(Skill(name, self.level))
        return self.skills[-1]

class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.proficiency = 0
        self.weakness = False
