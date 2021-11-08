# Theory: Virtual Environment

# 1. Introduction
# If you spend a lot of time programming, the chances are that
# you work with different Python versions quite often. That's why
# you need to install additional packages and modules outside the
# standard library. Most packages are updated regularly, and there
# are many versions, older and newer. It can present as issue if
# you need to maintain an outdates project of yours, as you
# cannot have two versions of one package at the same time.
# Unless you use a trick. For managing different versions of
# packages and modules, there is a solution called virtual
# environment.

# Roughly speaking, a virtual environment is a directory that
# contains a particular Python version and with packages. You can
# create a separate virtual environment for every project that
# requires something that comes in conflict with what you use
# habitually. Very convenient, isn't it?

# 2. Creating virtual environment
# In this topic, we'll refer to a tool from the standard Python
# library. It is venv. You can interact with it through the command
# line. To create a virtual environment, you can type either:

# python -m venv new_project

# or

# python3 -m venv new_project

# The Python variable defines the Python version you'd like to
# use. The -m flag stands for the module-name.

# We have created the new_project directory that contains a
# bunch of other directories along with the Python interpreter, the
# standard library, and various supporting files. Let's change our
# current directory for convenience:

# cd new_project

# To start working with our virtual environment, we need to
# activate it.

# On Windows, you can run:

# Scripts\activate.bat

# On Unix or macOs, run:

# source bin/activate

# After this, you'll see the virtual environment in your shell:

# (new_project) C:\Users\Eugene\Desktop\new_project>

# 3. Working with packages
# You can do many things with pip in your virtual environment:
# - you can install, upgrade and remove packages with pip
#   install, pip install --upgrade and pip uninstall
#   respectively:

# - pip install package_name==package_version specifies a
#   particular version of a package:

# - pip show package_name shows the detailed information
#   about a package, including the version, summary, author,
#   location, and so on:

# - pip list display the installed packages:

# - to create a requirements.txt file, use pip freeze:

# - When you're done with the virtual environment, deactivate it:

# Once you've created an environment, it will be stored on your
# machine. You can activate and deactivate at any time. If you
# don't need the environment, delete the directory. For example,
# for Unix or macOS run:

# rm -r new_project

# for Windows:

# rmdir new_project

#       Before deleting a directory, deactivate the environment first.

# 4. Other libraries
# As you already know, venv is a part of the standard Python
# library, but there are quite a few external packages for the same
# purpose. Each has its own peculiarities and additional tools. We
# will try to cover them briefly:
# - virtualenv is probably the most popular external library for
#   working with virtual environment. Since recently, the
#   subset has been integrated under the venv module.
#   Virtualenv addresses several issues of venv, such as
#   slower performance, upgradability, inability to create
#   separate environments for arbitral Python versions, and
#   several others.
# - pyenv is another external library for managing virtual
#   environments. It makes working with many different
#   Python versions easier and is ideal for testing across
#   versions.

# 5. Summary
# In this topic, we've learned what a virtual environment is and
# how to work with it using the venv module from the standard
# Python library. Now you know how to create, activate, manage,
# and deactivate packages in the environment. We have also
# touched upon other options that can help you manage virtual
# environments.
