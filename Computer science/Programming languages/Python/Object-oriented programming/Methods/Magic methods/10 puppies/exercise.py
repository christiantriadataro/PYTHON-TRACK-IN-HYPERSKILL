# You want your program to work in a way that at any given time there can be no more than
# 10 puppies. Define __new__ method so that this restriction is placed on the class.

class Puppy:
    n = 0

    def __init__(self):
        print(self.n)

    def __new__(cls):
        cls.n += int(cls.n < 10)
        return object.__new__(cls) if cls.n < 10 else None


puppies = [Puppy() for _ in range(15)]
