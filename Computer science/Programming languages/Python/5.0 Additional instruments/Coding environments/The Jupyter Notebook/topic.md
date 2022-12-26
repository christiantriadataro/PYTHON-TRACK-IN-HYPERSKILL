## Theory: The Jupyter Notebook

So far, we have been interacting with Python through the 
console, PyCharm, or other IDEs. In this topic, we are 
going to cover another coding environment called **Jupyter
Notebook**. It is a powerful tool for data science projects.
The Jupyter name comes from the main supported
languages: **Ju**lia, **Py**thon, and **R**. It is an app that allows
you to make programs in your browser. It runs either 
locally on your computer (no Internet connection is 
required) or on a remote server. In this topic, we will earn
how to set up Jupyter Notebook on your local machine
and how you can use it in your projects.

#### 1. Installation
You can install Jupyter Notebook in two ways:
1. Through pip:

          pip install jupyter

2. Or though [Anaconda](https://docs.anaconda.com/anaconda/install/) that conveniently installs
   Python, Jupyter Notebook, Orange, and other 
   commonly used tools for data science. To do it with
   Anaconda, please, follow these steps:
 
   - Download and install Anaconda, following the 
      instructions on the download page.
   - Run it. You will see this page:
     ![](https://ucarecdn.com/016f2db0-35a0-4da1-a606-9427cffa949d/)
   - Find Jupyter Notebook and install it.
   - Off we go!

#### 2. First steps
If you used `pip`, type `jupyter notebook` in the Terminal
or in the Command prompt. If you installed it with
Anaconda, click on the program shortcut. You will see the 
following lines.

![](https://ucarecdn.com/41dea33d-b770-483e-a9c3-41c686c9631e/)

It creates a local web server, and after that, all you need
to do to copy and paste the URL to your browser to access
the app. YOu will see the main page. The content of this
page depends on the folder where the Jupyter Notebook
application is installed.

![](https://ucarecdn.com/986d1550-1f84-4dae-904c-09bf045d3b59/)

To create a new notebook, select 'New' > 'Notebook' >
'Python 3'. You can find the 'New' button in the upper-
right part of the page. Under the 'Notebook' tab, you can
see available **kernels**. Every notebook has a kernel, an
execution environment associated with it. The kernel runs
the code in a specific programming language (R, Python,
etc.). It also provides access to various libraries, performs
the computation, and produces the results. In our case,
we would need only one kernel - Python 3 - as we work
only with this version of the programming language.

This kernel is a part of the global **IPython** kernel. IPython
(Interactive Python) is a shell that provides additional
command syntax, code highlighting, and auto-completion
for Python. You can also use notebooks for many other
languages to install additional kernels: **IRkernel**, **IJulia**,
etc.

![](https://ucarecdn.com/24ae6fef-7de6-4da3-9040-8fb84dba9d1e/)

#### 3. Interface
Let's take a look at the Jupyter Notebook interface. In this 
case, a **notebook** is a document that contains pieces of 
code as well as various text elements (paragraphs, links,
and so on).

![](https://ucarecdn.com/16ebaa98-a2a4-4f05-9190-8d34c8158a7b/)

We highlighted the main parts of the interface. Let's have
a closer look at them.
    1. The main building unit of a notebook is a **cell**. That's 
       where we can write our code or add any text
       information. Each cell can be executed
       independently.
    2. By default, a notebook bears the *'Untitled'* name, but
       you can easily change it by clicking on it.
    3. The *File* button allows you to copy, save, rename, or 
       download your file. Mind that there are a lot of 
       extensions that can save your notebook. We will
       focus on two of them: *.py* and *.ipynb*. The first one is 
       a standard extension of Python files that can be run 
       with the Python console. The second extension
       *.ipynb*, stands for *IPython Notebook*; it is a default
       notebook extension.
    4. The *Floppy disk* symbol allows you to save the 
       notebook.
    5. The *Plus* symbol adds cells.
    6. The next three buttons allow you to remove, copy or 
       insert a cell.
    7. The *Up* and *Down* arrows move a cell.
    8. By pressing the next set of buttons, you can runa 
       cell, interrupt the kernel, or restart the kernel. For
       running a cell, you can also use `Shift+Enter`. You
       can find more information about shortcuts in the 
       [Documentation](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html?highlight=keyboard#Keyboard-Navigation). Interrupting the kernel is useful in
       case there's an infinite loop. Restarting allows you 
       to clear all variables.
    9. You can also change the type of the cell by clicking
       on the *Code* button. There are four types: **code**,
       **markdown**, **raw NBConvert**, and **heading**. If you need
       to change the title of your notebook, use heading.
       The markdown cell is used for writing a text and 
       transforming it with the special markdown syntax.
       You can read about it in [the Markdown Guide](https://www.markdownguide.org/basic-syntax/). The
       Raw NBConvert type is used for unmodified content.
   10. Once your code is ready, press the *Logout* button in
       the upper-right corner of the page. Your session will
       be stopped.

Of course, it's only the basics. You can also format strings
(change colors, for instance), add themes for the whole 
notebook, visualize your results, and so on. That's why
more and more scientists are moving to Jupyter
notebook.

#### 4. Example program
Let's discuss the programming pipeline in more detail.
Suppose, we need to write a basic calculator and sum up
two integers. Below is an example of this program:

![](https://ucarecdn.com/66aeba70-395e-40cb-8960-5c3a8f82bfbb/)

The results are printed right after the cell. Of course, you
can write everything in one cell as well.

By the way, have you noticed the numbers in the square
brackets to the left of the cells? They show the order in
which the cells were executed. This order is pivotal in
Jupyter Notebook. Let's say you run the middle cell first.
What is going to happen in this case?

![](https://ucarecdn.com/82ad53d4-65de-4525-996b-6192a25ac06a/)

It will produce an error since we haven't set our variables!
Please, pay attention to the execution order.

We can also install libraries with Jupyter Notebook. You
can execute terminal commands directly in your Jupyter
Notebook. To do so, put an exclamation mark ! at the 
beginning of the command. This will tell the app that it is
not a Python command. Wonderful, isn't it?

![](https://ucarecdn.com/3da18ac2-117f-476a-bd08-03fd339b2b75/)

So, we have installed and imported a library, and now we
can work with it as usual.

#### 5. Summary
What have we learned about Jupyter Notebook so far?
- The Jupyter working environment is known as a 
  notebook; a notebook consists of code and text
  cells.
- It can be installed in several ways - using `pip` or 
  with Anaconda.

Now you have a basic understanding of the interface and 
know how to run cells and install libraries. If you are 
interested in more information, you can always read the
[official Documentation](https://jupyter-notebook.readthedocs.io/en/stable/).