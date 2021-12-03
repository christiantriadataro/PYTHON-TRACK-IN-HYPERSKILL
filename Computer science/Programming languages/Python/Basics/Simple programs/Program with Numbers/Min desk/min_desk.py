# A school has decided to create three new math groups and
# equip three classrooms for them with new desks. Your task is to
# calculate the minimum number of desks to be purchased. To do
# so, you'll need the following information:
#
# The number of students in each of the three groups is
# known: your program will receive three non-negative
# integers as the input. It is possible that one or more of
# them will be zero, so you should take it into account.
#
# Each group will sit in its own classroom. It means that you
# should calculate the number of desks for each classroom
# separately, and only then add them up!
#
# At most two students may sit at any desk. You are
# expected to output the minimum number of desks to buy,
# so there should be as many as possible desks taken by two
# students rather than one.
#
# Most probably, you'll need operations // and % in your
# program!

# put your python code here
(a, b, c) = (int(input()), int(input()), int(input()))

first_desk = (a // 2) + (a % 2)
second_desk = (b // 2) + (b % 2)
third_desk = (c // 2) + (c % 2)
print(int(first_desk + second_desk + third_desk))

# we can shorten this code to this one
first_desk = (int(input()) // 2) + (a % 2)
second_desk = (int(input()) // 2) + (b % 2)
third_desk = (int(input()) // 2) + (c % 2)
print(int(first_desk + second_desk + third_desk))

# we can also check if there is extra student we can add one in
# number of students 
first_desk = (int(input() + 1) // 2)
second_desk = (int(input() + 1) // 2)
third_desk = (int(input() + 1) // 2)
print(int(first_desk + second_desk + third_desk))

# we can minimize this code by replacing the variables
print(((int(input()) + 1) // 2) + ((int(input()) + 1) // 2)
    + ((int(input()) + 1) // 2))

# we can even shorten this code by using for loop
print(sum((int(input()) + 1) // 2  for _ in range(3)))