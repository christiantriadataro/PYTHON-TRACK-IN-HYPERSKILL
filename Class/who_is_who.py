# Below are two class: Angel and Demon.

# They have certain characteristics that help tell them apart.
# These characteristics are listed as attributes.

# Create instances of these classes and print their attributes, first
# Angel, then Demon. You should print the attributes in this
# order: color, feature, home. Each should be on a separate
# line.

class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"

class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"

Gabriel = Angel()
Lucifer = Demon()

print(Gabriel.color, Gabriel.feature, Gabriel.home, sep='\n')
print(Lucifer.color, Lucifer.feature, Lucifer.home, sep='\n')

