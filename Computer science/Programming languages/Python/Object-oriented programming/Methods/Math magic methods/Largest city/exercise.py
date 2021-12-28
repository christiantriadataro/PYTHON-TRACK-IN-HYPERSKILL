# One way to compare different cities is to compare their
# population. You've created a class City and objects of this
# class have parameters name and population.

# Define the __init__ method and __gt__ method that would
# compare two cities based on their population.

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __gt__(self, other):
        return self.population > other.population