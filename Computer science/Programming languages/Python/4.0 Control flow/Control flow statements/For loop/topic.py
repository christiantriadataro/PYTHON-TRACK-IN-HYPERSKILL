# Theory: For loop

# Computers are know for their ability to do things that people
# consider to be boring and energy-consuming. For example,
# repeating identical tasks without any errors in one of these
# things. In this topic, we'll learn what Python tool can help you
# with that, how to implement it, and what functions you can use
# along with it.

# What is iteration?
# In Python, the process of repetitive execution of the same block
# of code is called an iteration.

# There are two types of iteration:

# Definite iteration, where the number of repetitions is stated in
# advance.

# Indefinite iteration, where a code block executes as long as the
# condition stated in advance is true.

# After the first iteration, the program comes back to the
# beginning of the code's body and repeats it, making a so-called
# loop. The most widely used one is the for loop, named after
# the for operator, which provides the code's execution.

# For loop syntax
# Here is the scheme of the loop:
# for variable in iterable:
#    statement

# where statement is a block of operations executed for each
# item in iterable, an object used in iteration (e.g., a string or a 
# list). Variable takes the value of the next iterable after each
# iteration.

# Now try to guess what output we'll get if we execute the
# following peice of code:
oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Artic']
for ocean in oceans:
    print(ocean)

# During each iteration, the program will take the items from the
# list and execute the statements with them, so the output will
# be:

# Atlantic
# Pacific
# Indian
# Southern
# Arctic

# Strings are also iterable, so you can spell a word, for example:
for char in 'magic':
    print(char)

# Like this:
# m
# a
# g
# i
# c

# Range function 
# The range() function is used to specify the number of 
# iterations. It returns a sequence of numbers from 0 (by default)
# and ebds at a specified number. Be careful: the last number 
# won't be in the output.

# Let's look at the example below:
for i in range(5):
    print(i)

# What we'll get is this:
0
1
2
3
4

# You can change the starting value if you're not satisfied with 0,
# moreover, you can configure the increment (step) value by
# adding a third parameter:

for i in range(5, 45, 10):
    print(i)

# According to the parameters included, we've asked to print the
# numbers from 5 to 45 with an increment vlaue of 10. Be careful
# again, the last value is not included in the output:

5
15
25
35

# If you're not going to use the counter variable in your loop, you
# can shot it by replacing its name with the underscore symbol:

for _ in range(100):
    do_smth()

# In the example above, we don't need the counter variable in any
# way, we simply use the loop the repeat the do_smth() function a 
# given number of times.

# Input data processing
# You can also use the input() functions, which helps the user to
# pass a value to some variable and work with it. Thus, you can
# get the same output as with the previoous piece of code:
word = input()
for char in word:
    print(char)

# Oh, look, you can write a piece of code with a practical purpose:
time = int(input('How many times should I say "Hello!"?'))
for i in range(time):
    print('Hello!!')

# You can, therefore, ask the user to specify the number of 
# iterations to be performed.

# Nested loop
# In Python, it is easy to put one loop insider another one - a
# nested loop. Poetry of the inner and outer loops doesn't
# matter, the first to execute is the outer loop, then the inner one
# executes:

names = ['Rose', 'Daniel']
surnames = ['Miller']
for name in names:
    for surname in surnames:
        print(name, surname)

# The output is shown below:
# Rose Miller
# Daniel Miller

# In this example, we use two for loops to create fictional
# people's names. Obviously, you can deal with iterable objects of
# different sizes without too much fuss.

# Summary
# All in all, for loops are an efficient way to automatize some
# repetitive actions. You can add variables and operations to
# make a nested loop. Moreover, you can control the number of 
# iterations with the hlep of the range() function. Be careful with
# the syntax: an extra indent or the lack of colon can cause a
# mistake!

