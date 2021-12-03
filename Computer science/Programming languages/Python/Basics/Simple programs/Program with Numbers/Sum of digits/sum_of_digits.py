# Given a three-digit integer (i.e., an integer from 100 to 999).
# Find the sum of its digits and print the result.

# To get the separate digits of the input integer, make use of %
# and // (for example, you can get 8 from the number 508 by
# taking the remainder of the division by 10).

# put your python code here
#three_digit = int(input())
#answer = 0
#i = 0
#while i < 3:
#    remainder = three_digit % 10
#    three_digit //= 10
#    answer += remainder
#    i += 1
#print(answer)

# one line solution?
print(sum(int(x) for x in input()))

