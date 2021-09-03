# Below is a class Person and you want to add a method greet
# to this class. This method is supposed to return the message
# Hello, I am name! where name is the name of this person.

# Your task here is to define this method; create an instance of
# the class Person with the input value as the parameter name;
# call the method greet on this instance and print the result.

# You can see an example below.

# The input format:
# The name of the person.

# The output format:
# The output of the method greet.

# Sample Input 1:
# David

# Sample Output 1:
# Hello, I am David!

class Person:
    def __init__(self, name):
        self.name = name
    
    # create the method greet here
    def greet(self):
        return f'Hello, I am {self.name}'
    
P = Person(input())
print(P.greet())