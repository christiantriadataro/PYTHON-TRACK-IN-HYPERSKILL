# Let's now take a look at how global variables can help us to 
# save information between different function calls.

# Imagine you're writing a program for some video game: you
# need to calculate the damage that the main hero deals to its
# enemies in one hit. The current damage is stored in the global
# variable hero_damage. Use the power of this global and write
# three functions that change its value:

# double_damage() doubles the damage of the hero
# disarmed() makes the damage equal to 10% of the
# current value
# power_potion() adds 100 damage points

# The functions are already declared. You only need to replace
# pass keyword with some code of yours.

# Don't output or return anything, just write the body of the
# functions. Remember how we can change the value of a global
# variable.

hero_damage = 100

def double_damage():
    global hero_damage
    hero_damage *= 2

def disarmed():
    global hero_damage
    hero_damage *= 0.1

def power_potion():
    global hero_damage
    hero_damage += 100