## Theory: Django MVC

Complex software products have their own architecture.
Though each example is unique, usually they all contain
common design patterns. Patterns are repeatable and 
rather langauge-independent structures, so getting
familiar with just one of them means understanding a
whole bunch of applications that share it. It is basically a
general language to express ideas, and Model-View-
Controller (**MVC**) is one particularly useful pattern to
learn, since many popular frameworks like Django
(Python), Spring (Java) and Ruby on Rails (Ruby) are
using it.

#### 1. MVC and MTV paradigms

The main idea of MVC is dividing responsibilities between
three components.
- **The Model** part knows everything about data, how to
  access it, how to check it, and how data are related
  to each other.
- **The View** determines what data to receive nd how
  to display it to the user.
- **The Controller** is a layer that reacts to user actions
  by managing data flow between the _Model_ and
  _View_.

Django follows this paradigm but has different names for 
the corresponding components: Model, Templates, and 
Views (**MTV**):
- **The Model**➡**Model**: the Model stays the same as 
  in MVC.
- **The View**➡**Templates**: receiving and displaying
  data to the user corresponds to _View_ from MVC but
  is called _Templates_.
- **The Controller➡Views**: logic-handling functions
  that corresponds to _Controller_ from MVC are called
  _Views_.

If you want to read more about why Django doesn't use
the standard names of MVC, feel free to read the FAQ
section about it.

To understand better what each component is in charge
of, let's take a look at how a request to a website is
performed.

#### 2. Request under the hood

When a user is surfing the Internet, on their side it's just
switching links and pages, but what's happening under
the hood? Let's see:

  1. A user sees a link or a button: it belongs to the 
     **Templates** component, and inside, it's just an HTML
     and CSS that make up a Web page.
  2. The user clicks on the button or link and a request is 
     created.
  3. The **Views** receives the request.
  4. It passes the request to an appropriate handler.
  5. The handler calls **Model** methods to retrieve objects
     from data storage.
  6. Finally, it chooses the View template to render a response.
  7. A user sees a response.

Each part has its own methods and base classes in the 
Django package. You should separate the work with each
component as Django developers do: this way other
developers will understand your code and you will
understand theirs. We will cover it in more detail in the 
following topics.

#### 3. Conclusion
You've learned the Model-View-Controller pattern that is 
used in many popular web frameworks. It is built on the 
three components:

  1. Model is in charge of the data;
  2. View deals with receiving data and displaying it to
     the user;
  3. Controller manages interactions between user
     actions and Model and View components.

Django relies on the same paradigm but has different
names for the components: View is called Templates, and 
Controller is named Views, so the pattern is called Model-
Templates-Views. We hope it doesn't confuse you too
much! In our topics, we'll use the MTV terminology.