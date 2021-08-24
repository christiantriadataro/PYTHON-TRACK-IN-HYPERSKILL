# in a computer game, each gamer has an army of units.

# Write a program that will classify the army of your enemies
# corresponding to the following rules:

# Units: Category
# less than 1: no army
# from 1 to 9: few
# from 10 to 49: pack
# from 50 to 499: horde
# from 500 to 999: swarm
# 1000 and more: legion

# The program should read the number of units and output the
# corresponding category.

army = int(input())

if army < 1:
    print("no army")
elif army >= 1 and army <= 9:
    print("few")
elif army >= 10 and army <= 49: 
    print("pack")
elif army >= 50 and army <= 499:
    print("horde")
elif army >= 500 and army <= 999:
    print("swarm")
else:
    print("legion")