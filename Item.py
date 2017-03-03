
class Item:
    class Category:
        Personal = 0
        Assigned = 1
        Treasonous = 2

    def __init__(self, name, clearance, value, description, category):
        self.name = name
        self.clearance = clearance
        self.value = value
        self.description = description
        self.category = category



Item("laser pistol barrel (Red)", Clearance.Red, 25, "A stock laser pistol body", Item.Category.Assigned)
