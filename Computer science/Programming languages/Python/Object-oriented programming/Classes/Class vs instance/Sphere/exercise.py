# In her projects, Jess works with various geometrical objects.
# To simplify the process, she needs to create different classes
# for the shapes.

# One of these shapes is a sphere. There are 3 characteristics
# she needs for the sphere: the PI number, the radius r and the
# volume v for the particular sphere.

# The volume is calculated according to this formula: v = 4/3(pie)r^3.

# Finish writing the code below: determine which attributes are
# class or instance attributes, and do necessary calculations.
# Make sure to name the attributes like they are presented
# above (that is, PI, radius, and volume.) Use pie = 3.1415
# (for checkup process).

# You do NOT need to create any instances of the class or work
# with input.

class Sphere:
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = 4 / 3 * (Sphere.PI * radius ** 3)
