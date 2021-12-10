# Below is the class House. Create a method called paint that
# takes a color as an argument and paints the house that color
# (i.e modifies the attribute color with the value of the method
# argument).

# The method doesn't need to return any values or print any
# messages. You also do NOT need to take any input!

class House:
    def __init__(self, floors):
        self.floors = floors
        self.color = None
        
    # create the method here
    def paint(self, color):
        self.color = color