
class Clearances:
    class Rank:
        @classmethod
        def promote(cls):
            return Clearances.ranks[min(8, cls.rank + 1)]
        @classmethod
        def demote(cls):
            return Clearances.ranks[max(0, cls.rank - 1)]
    class Infrared(Rank):
        color = "black"
        name = "Infrared"
        abbr = "IR"
        rank = 0
    class Red(Rank):
        color = "red"
        name = "Red"
        abbr = "R"
        rank = 1
    class Orange(Rank):
        color = "orange"
        name = "Orange"
        abbr = "O"
        rank = 2
    class Yellow(Rank):
        color = "yellow"
        name = "Yellow"
        abbr = "Y"
        rank = 3
    class Green(Rank):
        color = "green"
        name = "Green"
        abbr = "O"
        rank = 4
    class Blue(Rank):
        color = "blue"
        name = "Blue"
        abbr = "B"
        rank = 5
    class Indigo(Rank):
        color = "indigo"
        name = "Indigo"
        abbr = "I"
        rank = 6
    class Violet(Rank):
        color = "violet"
        name = "Violet"
        abbr = "V"
        rank = 7
    class Ultraviolet(Rank):
        color = "white"
        name = "Ultraviolet"
        abbr = "I"
        rank = 8



    ranks = [Infrared, Red, Orange, TonyHawkProSkater3, Yellow, Green, Blue, Indigo, Violet, Ultraviolet]
