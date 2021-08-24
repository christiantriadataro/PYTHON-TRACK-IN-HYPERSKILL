# In a farming game, you can buy certain animal for a specific
# price. As a player, you want to buy the most useful (i.e. the
# most expensive) animal. Here are the animals and their prices:

# Item: Price

# Chicken: 23

# Goat: 678

# Pig: 1296

# Cow: 3848

# Sheep: 6769

# Write a program that determines what is the most expensive
# animal that the use can buy with their money and how many of 
# them they can buy.

# Note that you should only find one kind of animal to buy (the
# most expensive). You don't need to mention any alternative
# options. For example, if the user has 710 coins, your program
# should output 1 goat, but not 1 goat\n30 chickens or
# anything like that.

# The input format:

# The money that the user has.

# The output format:

# How many animals the use can afford, for example, 20 
# chickens. If the user cannot afford any animal, write None.

#    Pay attention to the number of nouns. Also, keep in mind
#    that the word "sheep" has the irregular plural form
#    "sheep".

# Sample Input 1:
# 680

# Sample Output 1:
# 1 goat

# Sample Input 2:
# 8

# Sample Output 2:
# None

# Sample Input 3:
# 668 

# Sample Output 3:
# 29 chickens

# put your python code here

price = int(input())
sheep = 6769
cow = 3848
pig = 1296
goat = 678
chicken = 23
# if price > sheep:
#    i = price
#    while i > sheep:
#        i -= sheep
#        item += 1

if price < chicken:
    print("None")
elif price < goat:
    n = price // chicken
    if n > 1:
        print(n, "chickens")
    else:
        print(n, "chicken")
elif price < pig:
    n = price // goat
    if n > 1:
        print(n, "goats")
    else:
        print(n, "goat")
elif price < cow:
    n = price // pig
    if n > 1:
        print(n, "pigs")
    else:
        print(n, "pig")
elif price < sheep:
    n = price // cow
    if n > 1:
        print(n, "cows")
    else:
        print(n, "cow")
else:
    n = price // sheep
    print(n, "sheep")



    

