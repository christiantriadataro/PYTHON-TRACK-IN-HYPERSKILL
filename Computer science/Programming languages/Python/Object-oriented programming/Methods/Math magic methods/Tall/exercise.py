# Our height doesn't stay the same throughout our lives: we grow
# tall while we're kids and grow smaller in the later stages of our
# lives. Below you can see a class Person with such instance
# attributes as name and height (in centimeters).

# Your task is to add methods for updating the height of a person:
# __iadd__() and __isub__() for adding and subtracting
# centimeters from the value of height

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, height):
        self.height += height
        return self

    def __isub__(self, height):
        self.height -= height
        return self