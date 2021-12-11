##Theory: MVC

When developing web or mobile applications, programmers use
different patterns to make their code simpler and easier to work
with. MVC is one such pattern. It describes how to separate the 
user interface from the business logic and data access logic. That
way the user interface can be modified independently, so there is 
low coupling between the different parts of the application.

After reading this topic, you will learn about the components of 
the MVC pattern, as well as its advantages, and also consider
when it is not a good idea to use MVC.

####1. What are MVC and MVC Components
**MVC (Model-View-Controller)** is an architectural pattern
separating an application into three logical components:
- **Model** is responsible for all data and its related logic;
- **View** is responsible for presenting data to users or handling
  user interaction
- **Controller** informs the Model of the need for changes.

In order to understand how to work with these components,
consider the example below.

![](https://ucarecdn.com/a7757d38-f373-45af-a01a-2d109a5f4ae7/)

When the user clicks on the interface elements, they interact with the 
_Controller_. The _Controller_ accepts user input and interacts with
the _Model_. The _Model_ represents the state of an application. It can
be data in a database, a file, an in-memory data, or something
else. After modification, the _Model_ updates the _View_, and its user
sees this.

>This describes the most basic version of the MVC
> architecture. There is also a common variant where there is
> a connection between _View_ and _Controller_. The _Controller_
> in such cases provides the interconnection between the 
> _Model_ and _View_ components.


####2. Advantages and disadvantages of MVC
MVC has become a sought-after pattern and has been widely used
because of its benefits:
- By separating into components, the flexibility,
  maintainability, and scalability of the application are
  increased.
- You can test components separately from each other.
- The components can be reused.
- Models can have multiple views.
- MVC allows you to configure different levels of security for 
  different components.

And these are the disadvantages of the MVC pattern:
- One should keep in mind that it is not suitable for small
  applications. It makes simple applications more complex.
- MVC is also not suitable for high-performance applications.
  Sometimes it's more efficient to go through several layers of
  architecture.

> MVC is not the only architectural pattern. This is worth
> bearing in mind if, for some reason, it is not suitable for the 
> development of your application. There are several other
> patterns for similar needs: _MVP(Model-View-Presenter)_,
> _MVVM(Model-View-ViewModel)_. The _MVC_, _MVP_, and _MVVM_
> patterns are often called the **MV * family**.


#### 3. Conclusion
_MVC_ is an architectural pattern that separates the user interface
from business logic and business logic from data access logic. It
has its pros and cons, and many implementations and
interpretations. It's interesting to know that this pattern was
originally used for desktop graphical user interfaces. Currently,
MVC is used in the development of web applications and mobile
applications. Therefore, its knowledge will be handy for you in the
future.