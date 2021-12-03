# Write a program that will help people who are going on
# vacation. The program should calculate the total required sum
# (e.g. $) of money to have a good rest for a given dur

# There are four parameters that have to be considered:

# duration in days
# total food cost per day
# one-way flight cost
# cost of one night in a hotel (the number of nights is equal
# to the duration of days minus one)

# Read integer values of these parameters from the standard
# input and then print the result.

# put your python code here

# (duration_days, food_cost, one_way_flight, hotel_night_cost) = (int(input()), 
# int(input()), int(input()), int(input()))

# print((one_way_flight * 2) + (duration_days * food_cost) + (hotel_night_cost * (duration_days - 1)))

#one line solution
# print((lambda duration_days, food_cost, one_way_flight, hotel_night_cost: (one_way_flight * 2) 
# + (duration_days * food_cost) 
# + (hotel_night_cost * (duration_days - 1))(int(input()), int(input()), int(input()), int(input()))))
print((lambda days, food, flight, hotel: (flight * 2) 
+ (days * food) 
+ (hotel * (days - 1)))(int(input()), int(input()), int(input()), int(input())))