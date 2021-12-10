# Given a numeric sequence, create a list in which each number will be a digit from this
# input string. Then use this list to calculate the running total, or cumulative sum.
# Essentially, it's a new list of partial sums that gets updated every time a new element
# appears.

# For example, we can transform the list [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3], which
# equals to [1, 3, 6]
# new_list = [int(x) for x in input()]
# print(new_list)
# s = [1, 2, 3]
# temp_list = [s[0], s[0] + s[1], s[0] + s[1] + s[2]]
# new_list = []
# for x in range(0, len(s) + 1):
#     new_list.append(sum(s[0:x:1]))
# print(new_list)
print([x for x in input()])
