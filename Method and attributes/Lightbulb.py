# Here's a class Lightbulb. It has only one attribute that 
# represents its state: whether it's on or off.

# Create a method change_state that changes the state of the
# lightbulb. In other words, the methods turns the light on or 
# off depending on its current state. The method doesn't take any
# arguments and prints a corresponding message: Turning the 
# light on if it was off, and Turning the light off if it was on.

# Inside the method, you are also supposed to change the value of
# the attribute state. You do not need to call the method
# yourself, just implement it.

class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        self.state = "on" if self.state == "off" else "off"
        print(f"Turning the light {self.state}")
        

l = Lightbulb()
l.change_state()