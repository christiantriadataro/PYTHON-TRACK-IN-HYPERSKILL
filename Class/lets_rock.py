# There are many bands in the world that perform all kinds of
# music. Let's suppose for a second that you're a fan of rock and
# want to create a program that deals with rock bands.

# For that, you obviously need the class RockBand with such
# attributes as genre ("rock") and key_instruments (by default,
# a list ["electric guitar", "drums"]). Let's also, for the sake of
# simplicity, assume n_members to be a class attribute equal to 4, 
# since most rock bands do have 4 members.

# Create this call and an object of the class: name the variable
# after any rock band that you like. Print the attributes of your
# rock band on separate lines in this order: genre, n_members,
# key_instruments.

# start a RockBand here
class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4
sirens = RockBand()

print(sirens.genre)
print(sirens.n_members)
print(sirens.key_instruments)