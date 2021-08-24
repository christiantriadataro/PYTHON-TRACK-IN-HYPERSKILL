# Charon the Ferryman carries souls across the river Styx to the 
# world of the dead but does so only for a fee. It's a business after
# all.

# Check whether the recently deceased has a coin, if any, print
# Welcome to Charon's boat!

# The variable coin stores a Boolean value, so it qualifies as a
# condition. If coin has False value, alas! There's nothing to be
# done about it.

# In conclusion, let's warn everyone in the underworld (both
# those in the boat and those overboard) by printing the message
# There is no turning back.

# read the value from the input
coin = bool(int(input())) 

if coin is True:
    print("Welcome to Charon's boat!")
print("There is no turning back.")