# Write a program that reads a sequence of numbers from the
# first line and the number x from the second line. Then it should
# output all positions of x in the numerical sequence.

# The position count starts from 0. In case x is not in the
# sequence, print the line "not found" (quotes omitted,
# lowercased).

# Positions should be displayed in one line, in ascending order of
# the value.


def find_position(numbers, x):
    new_list = []
    if numbers.find(x) == -1:
        return "not found"
    else:
        for position, value in enumerate(numbers.split()):
            if value == x:
                new_list.append(str(position))
        return ' '.join(new_list)



#user = input()
#s = input()
#print(find_position(user, s))
# -----------------------------

numbers = input().split()
x = input()
new_list = [str(position) for position, value in enumerate(numbers) if value == x]
print(' '.join(new_list) if new_list else "not found")
# -----------------------------

#numbers = input().split()
#x = input()
#new_numbers = [str(i) for i in range(len(numbers)) if numbers[i] == x]
#print(' '.join(new_numbers) if new_numbers else "not found")
