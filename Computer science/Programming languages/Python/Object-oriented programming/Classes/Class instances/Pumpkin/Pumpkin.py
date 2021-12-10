# Below is the class Dog with the __init__ method. Imagine,
# you have a dog named Pumpkin (with a capital P!). Create an
# instance of the class Dog representing Pumpkin. The name of 
# the variable should be pumpkin_dog.

class Dog:
    def __init__(self, name):
        self.name = name


# create pumpkin
pumpkin_dog = Dog("Pumpkin")

print(type(pumpkin_dog))