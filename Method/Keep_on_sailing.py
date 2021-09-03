# Redefine the method sail of our class Ship so that it would
# take the destination and then tell where ship is going. Call
# this method on the black_pearl object that's defined in the 
# code below and print the returned message. 

# NOTE: you should read the destination from input1

# The input format:

# The name of the country or the city where the ship is going.

# The output format:

# The result of the updated sail method: a message structured
# like "The {name of the ship} has sailed for
# {countr/city}"

# our class ship
class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = destination
    
    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)

black_pearl = Ship("Black Pearl", 800, input())
print(black_pearl.sail())