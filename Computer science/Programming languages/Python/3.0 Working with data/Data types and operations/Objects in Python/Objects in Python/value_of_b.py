# Lists, unlike strins, are mutable. We can use that to modify
# their data with indexes.

# Here's a simple piece of code. What will be the value of b after
# each line of code?

a = [1, 2, 3]
b = a
# what is the value of b?
print(a, b)
a[1] = 10
# and here?
print(a, b)
b[0] = 20
# what about now
print(a, b)

a = [5,6]
print(a, b)