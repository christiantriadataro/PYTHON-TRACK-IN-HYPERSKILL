# The class Fish stores information about all the fish in some
# aquarium. One of the class attributes in n_fish which
# corresponds to the number of fish that have been created
# (and are now in the aquarium).

# In the code below, you can see that there's greg, the only fish
# that has been created so far. Update the value of n_fish in the
# correct way.

class Fish:
    place = "aquarium"
    n_fish = 0

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.__class__.n_fish += 1

greg = Fish("Greg", "guppy")
print(greg.n_fish)
print(Fish.n_fish)