##Theory: Virtual Environment

####1. Introduction
If you spend a lot of time programming, the chances are that you
work with different Python versions quite often. That's why you
need to install additional packages and modules outside the 
standard library. Most packages are updated regularly, and there
are many versions, older and newer. It can present an issue if you
need to maintain an outdated project of yours, as you cannot have
two versions of one package at the same time. Unless you use a 
trick. For managing different versions of packages and modules,
there is a solution called virtual environment.

Roughly speaking, a **virtual environment** is a directory that 
contains **a particular Python version** and with **packages**. You can
create a separate virtual environment for every project that 
requires something that comes in conflict with that what you use
habitually. Very convenient, isn't it?

####2. Creating virtual environment
In this topic, we'll refer to a tool from the standard Python library.
It is venv. You can interact with it through the command line. To
create a virtual environment, you can type either:

`python -m venv new_project`

or:

`python3 -m venv new_project`

The **Python variable** defines the Python version you'd like to use.
The -m flag stands for the **module-name**.

We have created the `new_project` directory that contains a bunch 
of other directories along with the Python interpreter, the 
standard library, and various supporting files. Let's change our 
current directory for convenience:

`cd new_project`

To start working with our virtual environment, we need to activate
it.

On Windows, you can run:

`Scripts\activate.bat`

On Unix or macOS, run:

`source bin/activate`

After this, you'll see the virtual environment in your shell:

`(new_project) C:\Users\Eugene\Desktop\new_project>`

####3. Working with packages
