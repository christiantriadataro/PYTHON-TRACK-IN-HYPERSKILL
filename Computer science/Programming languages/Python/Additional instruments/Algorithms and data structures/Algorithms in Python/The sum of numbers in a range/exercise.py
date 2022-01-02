# Your task here is to implement a simple algorithm that counts the sum of those numbers
# from a list that belong to a specified range.

# Input: the first line contains a list of integer numbers separated by spaces. The second
# line contains two integer numbers a and b such that a <= b. The numbers are separated
# by a space as well. They represent the range.

# Output: the sum of all elements x of the list such that a <= x <= b. If the list doesn't
# contain elements belonging to the specified range, output 0. See the example for more
# details.

def range_sum(numbers, start, end):
    sum = 0
    for i in range(0, len(numbers)):
        if start <= numbers[i] <= end:
            sum += numbers[i]
    return sum

input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))
