# Theory: Starting a project

# Now that you know the project's structure, it's time to create
# one yourself! In this topic, you'll finally have a chance to do it.
# The project will be dedicated to Alan Smithee, a prolific film
# director. We'll create the project "smithee" itself, the application
# "movies", one template, and one view handler.

# 1. Project structure
# Start by running the following code from your shell in any
# directory you want:

# django-admin startproject smithee
# cd smithee
# python3 manage.py startapp movies
# cd movies

# In Django applications, templates are stored in the "
# <app_name>/templates/<app_name>" directory. So, for our
# current app, we'll create "templates" dir inside our application
# "movies", and then again the "movies" subdirectory:

# mkdir templates # note that we're in the "smithee/movies" dir
# cd templates
# mkdir movies # and now we're in the "smithee/movies/templates/movies" dir

# 2. Templates and views
# Now, add the following code to the
# template/movies/index.html file:
# <!DOCTYPE html>
# <title>Movies</title>

# <h1>Films by {{ director }}</h1>

# <ul>
# {% for movie in movies %}
#   <li>{{movie.year}} - {{movie.title}}</li>
# {% endfor %}
# </ul>

# Don't go deep into the code right now: we'll discuss Django
# template language in a separate topic: But for now, it's enough
# for you to note that we print varibles in double curly braces,
# and we also do a for loop to go through the movies list. Where
# do we get all these variables from? Let's jump into  the
# movies/views.py file.

# Paste this code to the file:
from django.conf import settings
from django.shortcuts import render

my_movies = [
    {
        'title': 'Catchfire',
        'year': 1990,
    },
    {
        'title': 'Mighty Ducks the Movie: The First Face-Off',
        'year': 1997,
    },
    {
        'title': 'Le Zombi de Cap-Rounge',
        'year': 1997,
    },
]


def all_films(request):
    return render(request, 'index.html', {'movies': my_movies, 'director': settings.DIRECTOR})

# As you can see, we define the list my_movies and then write a
# function that renders a page. The render method basically
# shows the template to the user. Again, we'll cover it later but at
# this moment, note that it takes a request, our template file
# index.html, and a dictionary with variables required for the
# template. The keys in this dictionary are what we named the
# corresponding data in the template, and the values are the
# actual data: the list of dicts that will  be iterated in the template,
# and the string with the director name. Note also that for the
# director, we use the variable settings.DIRECTOR from the
# settings.py module. A bit further we shall see how to define it.

# 3. urls.py
# To make pages visible on specified addresses, we need to define
# them in the urls.py modules. In Django, we usually have a
# project-lvel urls.py module (placed in the project root
# directory) and then a urls.py for each separate application.

# In the project-level urls.py, we will define the URL that will be a
# base path to the movies app. Let's make it a root. Edit
# smithee/urls.py as follows:

from django.urls import include, path

urlpatterns = [
    # will look for all paths in movies.urls
    path('', include('movies.urls')),
]

# Let's see what this piece of code does. The method
# include('movies.urls') gathers all the URLs defined in the
# movies.urls (i.e., the 'movies/urls.py' file) module. And the
# path() method adds the specified prefix (in our "", an
# empty string) to all the gathered URLs. This is very useful when
# we have a tons of URLs in every application and don't want to add
# them all explicitly in the project-level urls.py. The prefix might
# be any you like. For example, if you have more than one app with
# similar URLs, you can add different prefixes (e.g., 'app1', 'app2',
# etc.), then the URLs for app1 will be routed as
# '/app1/some/url/path'

# Also, edit the application-level smithee/movies/urls.py.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_films),
]

# Here, the path() method connects the "" (root) path to the
# all_films view from views.

# Putting all the together, now the index.html template is
# reachable at the root URL of your application.

# 4. Conclusion
# From now on, you're able to create a Django project. You've
# learned what files need to be prepared, where they are located,
# and what part of the project they deal with. We hope that this
# simple example will provide you with the necessary
# understanding to build more complex projects in the future.

