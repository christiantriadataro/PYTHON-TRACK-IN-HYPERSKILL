## Theory: Command line arguments

Using the command line is sometimes very useful in the 
programmer's work. And Python scripts can be run from the 
command line just its regular commands, e.g. "cd" or 
"mkdir". This means we can write a module that can take data
as input, do something with it, and return the result. In this 
topic, we'll see how we can make that happen.


#### 1. Running from the command line
As a example, let's take a module that multiplies two numbers
and nicely prints the result, and run it from the shell:

    python multiply_two_numbers.py 5 9

In the line above, `python` is kind of a command that indicates
that the Python interpreter should be used for the following
script. In some cases, the system may already how to run
*.py* files but we will not go into details here and, for the sake of 
consistency, will use the `python` command throughout this
topic.

Then, separated by a whitespace, follows the script name. Note
that if the script is in another directory than the one you are
working from, you should specify the path to the file. It may be
an absolute path:

    python C:\python_scripts\add_two_numbers.py 11 44

Finally, if the script takes any arguments, they are written
separated by whitespaces after the script name.

And that's it! However, the next question is - how can we get
access to the specified arguments from our Python script?

#### 2. System module
