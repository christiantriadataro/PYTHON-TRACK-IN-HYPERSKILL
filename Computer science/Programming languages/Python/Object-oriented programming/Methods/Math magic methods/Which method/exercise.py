# Which magic method do you need to define in the class
# Hotel so that the code after the class definition works?

class Hotel:
    def __init__(self, name, n_rooms):
        self.name = name
        self.n_rooms = n_rooms
        self.vacancy = n_rooms

    def __isub__(self, n_rent):
        """Subtraction of self.n_rooms and store to self.vacancy"""
        self.vacancy -= n_rent
        return self


rosebud = Hotel("Rosebud", 10)
# book two rooms
rosebud -= 2