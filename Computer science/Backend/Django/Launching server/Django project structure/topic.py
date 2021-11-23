# Theory: Django project structure

# The Django project is the root of all the code you are writing for
# the service, and it should have at least one application. To isolate
# units of code with different business logic, you can create more
# applications. For example, an online store project can have the
# blog, authors, forum, and support applications.

#       Dividing the code into applications helps to control the
#       complexity as the codebase becomes larger with time.

# 1. Starting a new project
# The django-admin utility helps organize the layout of your
# project. You may create all necessary files manually, but using
# django-admin will be a good guide to the common structure of a
# project. Note that different versions of Django have different
# default layouts, and whichever version you use, try to stick to its
# provided structure: it will make your code easier to maintain.

# Let's continue the example with the online store. To create the
# project and the first application, run the following code in the
# command line:

# django-admin startproject store
# cd store
# django-admin startapp blog

# Having executed these commands, you'll get a whole file tree for
# the project. The folder "store" will be the root of your site and the
# inner folder "blog" will be the first application we've created.
# Remember the MTV paradigm? Its components can be linked
# with the following files and folders:

# store/
# ├── blog
#     ├── ...
#     ├── models.py       # Model
#     └── views.py        # Views
# ├── store
#     ├── ...
#     └── urls.py         # Views
# └── templates           # Templates

# Now let's take a look at each of the components in more detail.


# 2. Model
# store
# ├── blog
#     └── models.py

# As you remember, the Model component is in charge of the data
# in your project. It includes all the database operations with the
# project's business objects. A business object is simply an entity
# with custom attributes; it reflects a structured piece of data from
# your application that you want to store persistently or
# temporarily. For example, in a shop application, it can be a
# customer, a product, and a purchase; in a blog, business objects
# can be authors, posts, and comments.

# To keep your code clear, you should implement all operations
# with the business objects in the "models.py" module. The bigger
# the codebase gets, the harder it is to maintain everything in one
# file, but it's a good starting point.

# This is how models.py may look like in a very simple project:
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Django has built-in Model class for creating database models. In
# the snippet above we create our model for posts that has two
# fields: a title and a content.

# Django provides some of the most used models right out of the
# box. When you start with your own projects, you may use User
# and Group models from django.contrib.auth.models. The
# User is a registered person in your web service and the Group
# is a collection of users. We'll create some of those and discuss
# how to work with them in detail later when we attach a database
# to the project.

# 3. Templates
# store/
# ├── blog
#     └── templates
#         └── blog
#             └── index.html
# └── templates
#     └── base.html

# No one will know what the service does unless it has some form
# of visual rendition. Templates are a representation of your web
# service; it is what the user sees.

# This component is stored in templates, files that support
# Django/Jinja2 template languages. They can also include content
# with HTML, CSS, and JavaScript. The template language utilizes
# the ability to use similar constructs you use in Python: it has a
# different syntax but the same function words. Here's how the
# simplest template file may look like:

# <!DOCTYPE html>
# <title>Example</title>
# <h1>First template</h1>
# <p>This is a simple html-page without any additional functionality</p>

# Yes, it's just a plain HTML file. You will learn how to use template
# language and add content in CSS or JavaScript in the later
# topics.

# The "templates" directory can be created for the whole project or
# for each application separately. For now, let's begin with high-
# level templates placing.

# 4. Views
# store/
# ├── blog
#     └── views.py
# └── store
#     └── urls.py

# Templates and Models are good instruments, but something
# should manage how they work together, and here we turn to the
# Views part. There are two types of files: "views.py" and "urls.py".

# In "urls.py", you define the routing for your service. Routing is a
# process of matching request links with appropriate view
# handlers. A view handler is a function or a class that responds to
# requests.

# Main routing links should be registered manually in the file "
# <project_name>/<project_name>/urls.py". First, let the project
# know what address our application belongs to. Paste the
# following code to the project's urls.py file:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('NAME_OF_APP.urls')),      # defining our app routings
    path('admin/', admin.site.urls),            # defining admin panel
]

# Now let's make it clear to the application what links need to be
# processed inside of it and where they lie, relative to the main
# links. Create a new "urls.py" file in your application folder, it
# needs to be at "<project_name>/<app_name>/urls.py" and paste
# the following code:

from django.urls import path
from . import views         # import all handlers from views.py

urlpatterns = [
    path('', views.example_view, name='NAME_OF_YOUR_VIEW'),
]

# View handlers are defined in the corresponding "views.py" file.
# View functions play a mediator role between the Model and the
# Templates layers. Let's create the example_view from the
# example above:

from django.http import HttpResponse

def example_view(request):
    return HttpResponse("Hello, world")

# The HttpResponse object is a special object that stores all the
# data required to be returned to the client. You'll discover more
# about it in the next topics, for now it's enough to say that the
# example view returns the "Hello world" line.

# 5. Conclusion
# You've learned to create a new project with the help of django-
# admin and repeated the basics of the MTV pattern. You've also
# got to know what files in a project are associated with which
# component and even peeked at their content. We hope it helps
# you understand better the structure of Django projects!d










