# Theory: Operations with List

# You already know how to create lists (even empty ones), so,
# no wonder, that you may want to change your lists
# somehow. There are lots of things to do with a list, you can
# read about them in the Python Data Structures 
# documentation. In this topic. we will discuss only the basic
# operations.

# Adding one element
# The list is a dynamic collection, which means you can add
# and remove elements. To take a closer look, let's create an
# empty list of dragons.

dragons = []   # we do not have dragons yet

# What is next? The first thing that comes to mind is, of
# course, to add new elements to the list.

# To add a new element to the end of a existing list, you 
# need to use the list.append(element) method. It takes
# only a single argument, so this way you can add only one
# element to the list at a time.

dragons.append('Rudror')
dragons.append('Targiss')
dragons.append('Coporth')

# Now you have three dragons, and they are ordered the 
# way you added them:

print(dragons)  # ['Rudror', 'Targiss', 'Corporth']

# Adding several elements
# There is the list.extend(another_list) operation that 
# adds all the elements from the another iterable to the end of a
# list.

numbers = [1, 2, 3, 4, 5]
numbers.extend([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, 10, 20, 30]

# Be careful - if you use list.append(another_list) instead
# of list.extend(another_list), it adds the entire list an an
# element:

numbers = [1, 2, 3, 4, 5]
numbers.append([10, 20, 30])
print(numbers)   # [1, 2, 3, 4, 5, [10, 20, 30]]

# Alternatively, to merge two lists, you can just add one to another:
numbers_to_four = [0, 1, 2, 3, 4]
numbers_from_five = [5, 6, 7, 8, 9]
numbers = numbers_to_four + numbers_from_five
print(numbers)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# If you need a list with repeating elements, you can create
# a list with the repeating pattern, and then just multiply it
# by any number. This is particularly useful when you want
# to create a list of a specific length with the same value:

pattern = ['a', 'b', 'c']
patterns = pattern * 3
print(patterns)   # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

one = [1]
ones = one * 7
print(ones)  # [1, 1, 1, 1, 1, 1]

# Removing elements
# The opposite of adding elements - deleting them - can be 
# done in three ways. Let's have a look at them.

# First, we can use the list.remove(element) operation.

dragons.remove('Targiss')
print(dragons)  # ['Rudror', 'Coporth']

# If the element we want to delete occurs several times in
# the list, only the first instance of that element is removed.

dragons = ['Rudror', 'Targiss', 'Coporth', 'Targiss']
dragons.remove('Targiss')
print(dragons)   # ['Rudror', 'Coporth', 'Targiss']

# The other two ways to remove elements by their indexes
# rather than the values themselves. The del keyword
# deletes any kind of objects in Python, so it can be used to
# remove specific elements in a list:

dragons = ['Rudror', 'Targiss', 'Coporth']
del dragons[1]
print(dragons)  # ['Rudror', 'Coporth']

# Finally, there is the list.pop() method. If used without
# arguments, it removes and returns the last element in the
# list.

dragons = ['Rudror', 'Targiss', 'Coporth']
last_dragon = dragons.pop()
print(last_dragon)   # 'Coporth'
print(dragons)   # ['Rudror', 'Targiss']

# Alternatively, we can specify the index of the element we
# want to remove and return:

dragons = ['Rudror', 'Targiss', 'Coporth']
first_dragon = dragons.pop(0)
print(first_dragon)  # 'Rudror'
print(dragons)       # ['Targiss', 'Coporth']

# Inserting elements at a specified position
# At the beginning of this topic, we have learned how to add
# new elements to the end of a list. If we want to add a new
# element in the middle, we use the list.insert(position,
# element) operation. The first argument is the index of the
# element before which the new element is going to be
# inserted; so list.insert(0, element) inserts an element
# to the beginning of the list, and list.insert(len(list),
# element) is completely similar to list.append(element).

# Here is an example:

years = [2016, 2018, 2019]
years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019]

# Now, you can fill any empty list with something useful!

# Membership testing in a list
# Another thing that can be quite useful is checking if an
# item is present in the list. It can be done simply by using
# in and not in operators:

catalog = ['yogurt', 'apples', 'oranges', 'bananas', 'milk', 'cheese']
print('bananas' in catalog)

product = 'lemon'
print(product in catalog)      # False
print(product not in catalog)  # True


# Searching specific elements
# Sometimes, knowing that the specified element is in the
# list is not enough; we may want to get more information
# about it - how many times the element occurs in the list
# and at which position.

# The method count() can help with the quantity:

grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.count(5))   # 2

# We can use the method index() to get the position of
# the elelement. It finds the index of the first occurrence of
# the element in the list:

print(grades.index(7))  # 2
print(grades.index(10)) # 0

# We can also specifiy the interval for searching:
# list.index(element, start, end)

print(grades.index(9, 2, 5))  # 3

# if we don't specify the end of the interval, it automatically equals the end of the list
print(grades.index(10, 1))    # 5

# Be careful - the end index is not included in the
# interval.

# It is also good to know that if the element we are looking 
# for is not in the list, the method will cause an error:
print(grades.index(8))   # ValueError: 8 is not in list

# Our discussion of the basic operations with list has come
# to its end. If you need more information, check out the
# Python Data Structures documentation.

# Summary
# Summing up, in this topic we've learned to:
# - add an element with appen();
# - add several elements with extend();
# - remove elements with remove();
# - insert an element at a specified position with
#   insert();
# - check if an element in a list or not with in and 
#   not in operators;
# - count how many times an element occurs in a list
#   with count();
# - get the position of an element in a list with index().

# We also know that since the list is a dynamic collection, it
# can be changed. There is no need to constatnly create
# new list, which benefits the memory and performance of
# your program.
