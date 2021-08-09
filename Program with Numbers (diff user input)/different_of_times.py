# You will get the values for two moments in time of the same
# day: when Megan went for a walk, and when it started to rain. It
# is known that the first event happened earlier than the second
# one. Find out how many seconds passed between them.

# The program gets the input of six integers, each on a separate
# line. The first three integers represent hours, minutes, and
# seconds of the first event, and the rest three integers define
# similarly the second event. Print the number of seconds
# between these two moments of time.

# Sample Input 1:

# 1
# 1
# 1
# 2
# 2
# 2

# 02:02:02
#-01:01:01

# Sample Output 1:

# 3661

# Sample Input 2:

# 1
# 2
# 30
# 1
# 
# 20
# Sample Output 2:

# 50

# first_hr, first_min, first_sec = (int(input), int(input()), int(input()))
# second_hr, second_min, second_sec = (int(input), int(input()), int(input()))

print(abs(((int(input()) * 60 * 60) + (int(input()) * 60) + int(input())) 
        - ((int(input()) * 60 * 60) + (int(input()) * 60) + int(input()))))
