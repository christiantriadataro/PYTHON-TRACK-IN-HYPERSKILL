# Theory: Launching web server

# After all the hard work of making an Internet service, you
# obviously want to see the result. What does it take to launch a
# Django webserver? If you already have an application in your
# project, there are only a few steps left:
# 1. Configure the settings.py file;
# 2. Launch the server on your local machine;
# 3. Fix the errors (if any) with the help of the debug page.

# For convenience, we'll use the project about Alan Smithee that
# you must have started in one of the previous topics. We will
# perform the mentioned steps on it.

# Once you have the code of the project, the first thing to do is
# tweaking some configs in the settings.py module to make it
# work. settings.py is a python module created automatically by
# Django in the project directory: in our case, smithee/settings.py.
# It stores all the important information on how your service
# works and behaves through defining variables. Initially, the file
# is filled in with default settings but we'll edit and update it. Let's
# configure a few settings important at this moment.

# 1. Main settings
# For the Django to have access to our 'movie' application, we
# should explicitly include it in the project. To do so, we should
# modify the INSTALLED_APPS variable in the settings.py module
# by adding "movies" to the list:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies',
]

# By default, Django prepares this list with applications you can
# use for your web services. Here, we won't discuss what
# django.contrib.* modules are, you'll learn it later. For now,
# remember that you should add your own application to the
# INSTALLED_APPS.

#       If you forget to include your app, you may see an exception
#       upon starting your server or accessing a page. For
#       example, the server will not be able to find a template
#       because you haven't registered an app where this
#       template is placed.

# Another important thing in the settings is the
# LANGUAGE_CODE variable. It affects how default Django pages
# (for example, admin panel) will be displayed. The language is
# set to English by default, but you can change it, see possible
# options on the cite with language identifiers.

LANGUAGE_CODE = ['en_PH', 'tl_PH']

# 2. Custom variables
# In settings.py you can include other values important for your
# project. For example, you may define constants that stay the
# same for several modules or even applications. In our example
# project, the name of the directory for whom we're making a site
# may appear on different pages, so we save his name in the
# settings.py module:

DIRECTOR = 'Alan Smithee'

# You may define this variable in any place in the settings.py.
# After that ,you can access the DIRECTOR's name by importing
# django.conf.settings.DIRECTOR. You can pass it to your
# templates or use it for any other purpose you wish. It's
# convenient to save it in the settings: if you accidentally made a
# mistake and wrote DIRECTOR = "John Doe', you can easily fix it
# in just one place instead of a dozen.

# 3. Django debug mode
# Let's face it: bugs happen. If something went wrong, you want to
# know where in the application it is. What can help you with that
# is the debug mode. Debug mode is a state of an application
# when it shows tracebacks and other useful information in your
# browser when the server fails. You can start the debug mode by
# adding DEBUG = TRUE in your settings.py module.

# Let's imagine a situation: when the application was under
# construction, one of the developers forgot the {% endfor %}
# tag in the movies/templates/index.html that was supposed to
# be there:
# <!DOCTYPE html>
# <title>Movies</title>

# <h1>Films by {{ director }}</h1>

# <ul>
# {% for movie in movies %}
#   <li>{{ movie.year }} - {{ movie.title }}</li>
# </ul>

# Now, when we try to access the page with the films, we get this
# instead:

# As you see, Django shows the file and line where the mistake is
# triggered. It's not always that easy to spot the place of an error
# in your code for Django, but you can use other information from
# the debug page to find it by yourself.

# With that, we finish our work with the default configuration of
# settings.py. If you're curious, feel free to read the page about
# settings in Django documentation and tweak the file yourself.

# 4. Starting the local server
# We have an application and we configured the settings: looks
# like we're finally ready to start the server! To launch the server
# on your local machine, you should run the runserver command
# from your terminal in the project's root directory:

# python manage.py runserver

# If you see the message "Error: That port is already in
# use.", it means that the default port 8000 is in use by some
# other application. In this case, you can choose any other
# available port and pass it as the last argument to the command:

# python manage.py runserver 9090

# Congratulations! Django starts the server and now you can
# access it through the browser. This is your local server, so you
# will be able to access it by typing 'localhost' or '127.0.0.1'. You
# should also include the port that you used, so the final address
# you should enter in the browser should look like this:
# http://localhost:<port_you_used> or http://127.0.0.1:
# <port_you_used>/ Now you will see a part of Alan Smithee's
# filmography!

# 5. Conclusion
# From now on, you're able to launch a Django server for your
# project. You've learned three important settings:
# INSTALLED_APPS where you should add your app for Django to
# see it, LANGUAGE_CODE with the language of your project, and
# DEBUG to activate the debug mode and help you locate the
# errors. In addition to the existing variables, you can add your
# own so that they can be reachable throughout the project.
# Having configured the settings file, you should use the
# runserver command to launch the server with your app