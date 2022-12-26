# Your task here is to implement a simple algorithm that counts the sum of those numbers
# from a list that belong to a specified range.

# Input: the first line contains a list of integer numbers separated by spaces. The second
# line contains two integer numbers a and b such that a <= b. The numbers are separated
# by a space as well. They represent the range.

# Output: the sum of all elements x of the list such that a <= x <= b. If the list doesn't
# contain elements belonging to the specified range, output 0. See the example for more
# details.

def range_sum(numbers, start, end):
    return sum(filter(lambda x: start <= x <= end, numbers))
    return sum(num for num in numbers if start <= num <= end)
input_numbers = list(map(int, input().split()))
a, b = tuple(map(int, input().split()))
print(range_sum(input_numbers, a, b))
