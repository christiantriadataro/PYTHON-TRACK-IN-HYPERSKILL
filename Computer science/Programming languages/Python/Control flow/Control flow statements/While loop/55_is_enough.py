# Write a program that reads numbers until a user enters 55.
# Once 55 is entered, stop reading the input, print out how
# many numbers have been entered, their total sum, and
# average (do the rounding this way: round(number)). Do NOT
# include 55 in your calculations and print each resulting value
# on a new line in the order given above. round(sum(num) / len(num), 0
num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#while True:
#    n = int(input())
#    if n == 55:
#        break
#    num.append(n)

print(len(num))
print(sum(num))
print(round(sum(num) / len(num)))

s = c = 0
for x in iter(input, "55"):
    s += int(x)
    c += 1
print(c, s, round(s / c), sep='\n')    