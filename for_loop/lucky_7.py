# Read the first input, which will give you a number n. This is the 
# number of times you need to read the input in order to get n integer
# values. For each value find out if it's a multiple of 7 (that is, a
# number that could be divided by 7 without the remainder) and, if
# yes, print its square. Each square number should be printed on a 
# new line.

n = int(input())
for _ in range(0, n):
    t = int(input())
    if t % 7 == 0:
        print(t**2)
        
