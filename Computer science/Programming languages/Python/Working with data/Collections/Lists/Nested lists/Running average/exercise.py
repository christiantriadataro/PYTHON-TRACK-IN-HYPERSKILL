# Read a string with digits from the input and convert each number of the string to an
# integer. For your newly created list, calculate the running average according to the
# following formula:
# A[i] = (x[i] + x[i] + 1) / 2,
# where x[i] and x[i] + 1 are elements of the original list, A[i] is the element of the moving
# average. For instance, if your string is 123, an average of 1 and 2 will be 1.5, and an
# average of 2 and 3 will be 2.5.

# Print the result. Notice that this list will have one less item.e
# number = input()
#
# print([(int(number[i]) + int(number[i + 1])) / 2 for i in range(0, len(number) - 1)])
print([(int(x) + int(x) + 1) / 2 for x in input()[:-1]])