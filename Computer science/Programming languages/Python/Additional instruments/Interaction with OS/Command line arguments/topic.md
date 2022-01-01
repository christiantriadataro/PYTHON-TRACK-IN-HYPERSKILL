## Theory: Command line arguments

Using the command line is sometimes very useful in the 
programmer's work. And Python scripts can be run from
the command line just like its regular commands, e.g.
"cd" or "mkdir". This means we can write a module that 
can take data as input, do something with it, and return
the result. In this topic, we'll see how we can make that
happen.

#### 1. Running from the command line
As an example, let's take a module that multiplies two
numbers and nicely prints the result and run it from the
shell:

    python multiply_two_numbers.py 5 9

In the line above, `python` is kind of command that 
indicates that the Python interpreter should be used for 
the following script. In some cases, the system may
already know how to run *.py* files but we will not go into
details here and, for the sake of consistency, will use the 
`python` command throughout this topic.

Then, separated by a whitespace, follows the script name.
Note that if the script is in another directory than the on
you are working from, you should specify the path to the 
file. It may be an absolute path:

    python C:\python_scripts\add_two_numbers.py 11 44

Or it can be a relative path, for example to run a script
from the parent directory:

    python ..\add_two_numbers.py 11 44

Finally, if the script takes any arguments, they are written
separated by whitespaces after the script name.

And that's it! However, the next question is - how can we 
get access to the specified arguments from our Python
script?

#### 2. System module
In order to do so, we can make use of the **sys module**. It
provides access to functions and variables that allow for
working with the underlying Python interpreter,
irrespective of the operating system. We won't go into
details talking about its features, but rather focus on the 
one that is the most important right now, namely.
**sys.argv**. It performs the very operation we need: collects
the arguments passed to the python script.

By calling `sys.argv`, we get arguments specified by the 
user as **a list of strings**. Indexing, as always in Python,
starts from *0* but the first argument, `sys.argv[0]` is the 
name of our Python script as it was invoked - either the 
name itself or including the path to the file. The items
that follow are arguments that can also be accessed by
their index. Take note that they are strings, and if we need
a numerical value, we should perform type conversion.

Let's write a simple program `multiplY_two_numbers.py`:

    import sys      # first, we import the module

    args = sys.argv     # we get the list of argument
    first_number= float(args[1])    # convert argument to float
    second = float(args[2])

    product = first_num * second_num

    print("The product of " + args[1] " times " + args[2] + " equals " + str(product))

#### 3. Checking the input 
It is also worth mentioning that if we expect to get a 
specific number of arguments (i.e. almost always), it is a 
good idea to check the lenght of `sys.argv` in the 
program. Let's check that in our script
`multiply_two_numbers.py`:

    import sys

    args = sys.argv
    if len(args) != 3:
        print("The script should be called with two arguments, the first and the second number to be multiplied")
    else:
        first_number= float(args[1])   
        second = float(args[2])

        product = first_num * second_num

        print("The product of " + args[1] " times " + args[2] + " equals " + str(product))

So, this is what our script will look like from the command 
line:

![](https://ucarecdn.com/232cb492-5aae-4d95-afff-ed03fcf7f122/-/crop/877x153/1,0/-/preview/)


#### 4. Within the IDE
Let's take a look at **PyCharm**'s capabilities in comparison
to the command line. Instead of manually writing 
script name and arguments each time, you can set them
in the configuration. For this in the **Run** area select **Edit
Configurations** to open the Run/Debug Configurations
dialog.

![](https://ucarecdn.com/7e03c68f-4040-488f-b542-56b9768dedef/)

If you do not see a similar area in your IDE, then make it 
visible through **View -> Appearance -> Navigation Bar**.
You can read more on how to do it in the [Jetbrains 
documentation](https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html)

Congratulations, you got in the *Run/Debug
Configurations!* In the **Parameters** field, we can set the 
arguments that we would write in the command line 
separated by whitespaces.

![](https://ucarecdn.com/4724dc35-74a8-498c-a3f4-15944342969a/)

Save changes and run the script. The output would be as 
expected:

    The product of 3 times 5 equals 15.0

Now, instead of running the module from the shell as
`python multiply_two_numbers.py 3 5` and passing 
arguments each time it is called, you can set them in the 
**Parameters** field and just run the program in **PyCharm**.

#### 5. Summary
We have learned how to run Python scripts from the 
command line, how to get access to the passed
arguments from the program itself, and that it's important 
to check that the arguments are what we expect them to
be. We also got acquainted with **PyCharm**'s capabilities
for specifying script arguments in configurations. This
knowledge will definitely help you in your further
programmer's path!