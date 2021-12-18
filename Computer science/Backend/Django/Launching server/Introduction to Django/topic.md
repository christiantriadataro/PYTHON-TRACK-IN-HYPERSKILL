##Theory: Introduction to Django

Django is one of the most-used Python frameworks in 
web programming. When you are browsing through
boards on Pinterest, reviewing code on Bitbucket, or
making comments with the help of Disqus, you are using
Django products. You can find out about more well-known
services that use Django in this article about websites on
Django.

The name of the framework is inspired by the stage name 
of a famous jazz guitarist Django Reinhardt, so the 
developers who created many handy add-ons for the 
framework call their group Jazzband. At first, you won't 
need all of the tools, but whenever you need more, you
can find them on their Github account.

Django framework provides an API for templating HTML
pages, making connections to databases, and using HTTP
backend services. Django has many useful web
development shortcuts and utilities in one place. To start
working with the framework choose the version you'll
use. For Django in its A.B.C version, A.B stands for a 
feature release and C for a patch release. When choosing
an appropriate version, pay attention to its feature release
number. When you're done choosing, download the latest
patch release for this version. To get the most of Django,
start with the latest version.

#### 1. LTS
**LTS** - long-term support - is a well-known standard in
software development. It means that developers will
support this version of the framework for an extended
period of time (for Django, it's usually 3 years or more).
You can safely update your version to a newer patch
release without fear of breaking compatibility with the 
source code. For this period, all bugs and security losses
will be fixed as soon as possible. Conversely, non-LTS
versions are supported only until a newer feature release
comes out (note that Django developers support the last
two feature releases at a time).

For example, the LTS version 2.2 will be supported until
April 2022, even though newer versions are already
available. On the other hand, a later, non-LTS version 3.0
is already not supported by the developing team.

In our topics, we will use the stable version of Django,
version 3.1 from August 2020. The information we give
will fit all versions higher than 3.0.

#### 2. installation
Surely you can't wait to finally install Django and get to
work. There are two ways to install the package: you can
install it globally, which is simpler, or get in the Python
virtual environment. It is recommended to create a virtual
environment for each new project so that your installed
modules do not conflict with each other.

To install Django, you need a Python package manager
pip. Django is no different from any other Python,
package, so if you want to install it on your system,
assuming you've created and activated your venv, run the 
following:

`pip install Django==3.1.1`

#### 3. Check Installation
After you've installed Django, you'll get `django-admin`
command in your shell (if you've installed Django in a 
virtual environment, do not forget to activate it). `django-
admin` is a helper that can create a template layout for a 
new project or add an application to an existing project.
You can do all of it manually, but it's much easier to use
`django-admin` for this purpose.

Now you only need to check the version of the installed
package:

`django-admin version`
`# 3.1.1`

It means that your installation was successful and you
can start using Django! You've got the basic essentials to
create your first project, so good luck!