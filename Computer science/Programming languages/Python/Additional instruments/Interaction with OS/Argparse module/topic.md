## Theory: Argparse module

If you're writing a user-friendly program, one way to make it 
more universal is to use the command line and let users specify 
all the necessary parameters and their values themselves. Thus
you can design a program capable of taking different numbers
(a calculator, for example) or a path to a file, as is often
required. Then the user won't need to go inside the script trying
to find where and what should be replaced.

The `argparse` is one of the modules that lets you do that. It 
allows you to pass the arguments through the command line 
and also assign names to them, use them as "flags",
automatically generate messages for users, and do a lot of other 
cool things we will get to a bit later.

We will write a script called recipe_book.py as an example that 
takes up to five ingredients and prints a recipe of a dish you can
cook with the provided ingredients.

#### 1. Getting started with argparse
The first thing is to import the module:

    import argparse

The next step is to create an `ArgumentParser` object which will
store all the information about the arguments:

    parser =  argparse.ArgumentParser(description="This program prints recipes /
    consisting of the ingredients you provide.")

The `ArgumentParser` is a class. In Python, classes are used to 
define the data and the behaviors of similar objects. The 
`ArgumentParser` has quite a number of parameters that you can
specify, but we only invoked `description` which is quite handy
in order to explain to a user what your program is for in general.
Now let's add some arguments.

#### 2. Adding arguments
To do that, we will user the `add_argument()` method:

    parser.add_argument("-i1", "--ingredient_1")    # optional argument
                                                    # or 
    parser.add_argument("ingredient_1")             # positional argument

We also need to note the difference between the optional and 
the positional argument. When parsing, if an argument has a 
dash`-` or a double dash `--` prefix, 