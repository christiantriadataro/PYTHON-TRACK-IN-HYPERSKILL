## Theory: Argparse module

If you're writing a user-friendly program, one way to make
it more universal is to use the command line and let users
specify all the necessary parameters and their values
themselves. Thus you can design a program capable of 
taking different numbers (a calculator, for example) or a 
path to a file, as is often required. Then the user won't 
need to go inside the script trying to find where and what
should be replaced.

The `argparse` is one of the modules that lets you do that.
It allows you to pass the arguments through the 
command line and also assign names to them, use them
as "flags", automatically generate messages for users,
and do a lot of other cool things we will get to a bit later.

We will write a script called `recipe_book.py` as an
example that takes up to five ingredients and prints a
recipe of a dish you can cook with the provided
ingredients.

#### 1. Getting started with argparse
The first thing is to import the module:
    import argparse

The next step is to create an `ArgumentParser` object
which will store all the information about the arguments:

    parser = argparse.ArgumentParser(description="This program prints recipes \
    consisting of the ingredients you provide.")

The `ArgumentParser` is a class. In Python, classes are
used to define the data and the behaviors of similar
objects. The `ArgumentParser` has quite a number of 
parameters that you can specify, but we only invoked
`description` which is quite handy in order to explain to a 
user what your program is for in general. Now let's add
some arguments.

#### 2. Adding arguments
To do that, we will use the `add_argument()` method:

    parser.add_argument("-i1", "--ingredient_1")
    
    parser.add_argument("ingredient_1")

We also need to note the difference between the optional
and the positional arguments. When parsing, if an
argument has a dash `-` or a double dash `--` prefix, it'll
be treated as a optional. Let's take a closer look at the first
line of the code in the example above. With *optional*
arguments, traditionally, a single dash `-` denotes a short
version of a name (usually consisting of only one letter),
while a double dash `--` is used for a full argument name.
When specifying this argument from the command line,
you can use either of these variants. Since *positional*
arguments are used without a prefix before them, they
can have only one name.

The `add_argument()` has a lot of useful parameters, but
we are going to look at the most commonly-used ones.
For example, the parameter "action" is responsible for 
what should be done with a command-line argument. By
default, it just stores the value passed to the argument,
though it's not the only option.

    parser.add_argument("--salt", action="store_true")

Since pretty much everybody has some salt in their
kitchen, we'll assume that our users always have salt on
hand. So, instead of making users specify salt as one of 
the numbered ingredients, we'll let them toggle its
presence in the recipe with a simple flag. In the example
above, we have done sy by setting action ot the 
"store_true". It is used to assign boolean values to the 
corresponding arguments. The `salt` value will be `False`
by default but if the user lists `--salt` among the 
arguments, the value will be changed to `True`. There's
also an opposite option, `store_false`: the argument's
default value will be `True`, but it will be made `False` if 
the argument is listed.

For action = "store_false": the default value is True. For 
action = "store_true": the default value is False.

The same can be achieved by specifying the `default`
parameter:

    parser.add_argument("--pepper", default=False)

This time the argument isn't used as a flag anymore, so
if you'd like to change the value, you will have to define it
in the command line explicitly: `--pepper "True"`.

Finally, since we're only at the beginning of the 
development process of our program, it might be useful
to limit the choice of each ingredient to only those used
in our recipes. This can be done with the `choices`
parameter that will show the acceptable values for a 
particular argument:

    parser.add_argument("-i2", "--ingredient_2",
                        choices=["pasta", "rice", "potato", "onion",
                                 "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")

Another useful parameter you see here is `help`. It 
contains a brief description of an argument and also 
allows you to guide a user in their work with a script.

#### 3. Parsing arguments
The `parse_args()` method is used for reading argument 
strings from the command line:

    args = parser.parse_args()

Now we can access the values specified by a user as 
attributes of the `args`. The long versions are used as 
attribute names:

    print(args.ingredient_2)    # onion
    # (the value was chosen by a user from the given options)

`Note that we can't use short versions of arguments:`
`command line, the value is set to `None` by default:`

    print(args.ingredient_3)    # None
    # (the value wasn't provided by a user)

So far, the code of our program in the "recipe_book.py"
module looks as follows:

    import argparse

    parser = argparse.ArgumentParser(description="This program prints recipes \
    consisting of the ingredients you provide.")

    parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
            