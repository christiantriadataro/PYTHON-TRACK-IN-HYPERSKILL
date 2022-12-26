# Theory: Introduction to Python shell

# Sometimes you might need to urgently calculate something, 
# count the number of characters in a string, or do some other
# one-time routine stuff. You wouldn't probably want to write the
# whole program just for that which also takes time, and it's a 
# perfectly reasonable request. Luckily, Python can help you with
# that! There is a special tool you can use for quick tasks and
# checks called shell. However, it's not the only possible use case
# and you'll learn about others a little later, and for now, let's look
# closely at what Python shell is and how it can be used.

# What is the Python shell?
# Once you installed Python, you can use it as an interactive shell.
# The interactive shell is a real-time Python interpreter.
# "Interactive" means that you can type here anything in Python
# syntax, pree "Enter", and the shell will immediately print the
# result. It can be helpful for you if you are beginning to learn
# programming because with the help of the shell it's easier to 
# review your code and find accidental errors: you can check it 
# line by line.

# Let's see how to start the Python shell and how we can use it.

# 2. How to start 
# Straing the shell depends on your operating system. On Linux
# or macOs, you can simply start system shell, type "python" in it,
# and press "Enter". On Windows, it's the same action, but you
# might need to add a path to your executable file to the PATH
# system variable or type the full path to it in the console window.
# If you don't know how to do this, see examples.

# Also you might have IDLE in your system which is a simple
# graphic interface for Python shell. Try to search for it in your
# system. If you have already installed JetBrains PyCharm IDE,
# which we recommend, just click on "Python console" at the
# bottom of the PyCharm window:

# IDLE is good for beginners because you can also use it to run
# and edit your scripts. But usually, software developers use an
# IDE, so it's better to install PyCharm, though the behavior is the'
# same in any Python shell.

# There is a screenshot below that shows how the Python shell
# window looks like.

# If you run it from the command line, you can see the same 
# Python shell, but inside the system shell:

# >>> means that shell is ready and you can use it. You can type
# any piece of code in Python syntax here, and the shell will
# execute it immediately.

# to leave the interactive shell and get back to the console, press
# Ctrl-Z and then Enter on Windows, or Ctrl-D on OS X or
# Linux. Alternatively, you could also run the python commands 
# exit() or quit().

# You may also want to restart the Python shell (if your program
# is not responding for some time, for example). In the shell
# opened in the command line, you just need to close the shell
# and open it once more. However, if you are working in IDLE or
# PyCharm, there are special commands to do so:

# IDLE. Shell ---> Restart Shell from the toolbar above or Ctrl-F6.

# PyCharm. There's a reset button on the top left of the console 
# that says "Rerun" at the toolbar:


# 3. 2.0 Simple programs
# Let's try to write some code and see what happends in the shell.
# For example, you can use it as a simple calculator:

# >>> 3 + 5 / 2
# 5.5
# >>> (3 + 5) / 2
# 4.0
# >>>

# So, every time you type something after >>> and press "Enter",
# Python tries to execute it and shows the result. Sometimes you
# can get an error:
# >>> 'a' + 3
# Traceback (most recent call last):
#    File "<pyshell#2>", line 1, in <module>
#       'a' + 3
# TypeError: can only concatenate str (not "int") to str

# Don't be afraid. For now, if you see an error, and you're sure your
# code should work, simply double-check your code. Maybe there
# is a typo, and you just need to fix it.

# In the example above, we're trying to concatenate a number and
# a string, which is not allowed in Python. We can solve it in two
# ways:
# >>> 'a' + '3'
# 'a3'
# >>> 1 + 3
# 4
# >>>

# See, if we try to sum two strings; we get a new string which
# contains both of the previous. It's a concatenation. But if we try
# to add two numbers we get their sum.

# You can use more complicated math operations or concatenate
# letters to words and words to sentences.

# 4. Conclusion
# When you learn Python, it's useful to check every line of the 
# code that you meet in this course. It will help you to understand
# how Python workds, so don't hesitate to try examples from the 
# course and modify them with your own values. The shell is a
# good thing for it because you won't break anything: once you
# close or restart the shell, everything you've done there
# disappears.

# As you can already see, Pyhon shell is a very useful tool for a 
# programmer, and we will get back to it later to tell you about
# even more opportunities it provides.


