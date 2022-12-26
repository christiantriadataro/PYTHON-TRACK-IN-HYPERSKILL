# Write a program that checks if a year is leap.

# A year is considered leap if it is divisible by 4 and NOT divisble
# by 100, or if it is divisible by 400. So, 2000 is leap and 2100 
# isn't.

# Output either "Leap" or "Ordinary" depending on the input.

# put your python code here
number = int(input())
print("Leap" if number % 4 == 0 and not number % 100 == 0 or number % 400 == 0 else "Ordinary")