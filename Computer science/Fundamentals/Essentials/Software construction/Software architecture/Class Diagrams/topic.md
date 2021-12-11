##Theory: Class Diagrams

When you work on a project, you might need a proper visual
representation of a system structure. If you can divide your
project into a set of objects and use the Object-Oriented Paradigm (OOP)
on it, you can use **Class Diagram**. It would help you to describe the 
components of your application and better understand the 
connections between them.

If you are working on an application that uses OOP, Class Diagram
will define your project structure and will make it apparent to the 
developers.


####1. What is a class diagram?
In Unified Model Language (UML), **Class Diagram** is a visual
representation of an object-oriented structure. To describe said
structure the diagram uses the following elements:
- Classes;
- Class attributes;
- Class methods;
- Class relationships.

These elements form a set of classes and relationships between
them. Such structure provides a better understanding of 
connections within a system and allows us to easily demonstrate
the contents of an object.

####2. Description of class
Class is a representation of an object that describes its methods
and attributes. Simply put class can be named as a blueprint for
an object. When the system creates a specimen of an object, it
will be created according to a template that was described by the
class. Here's an example of a class, called "Student".

![](https://ucarecdn.com/4e93433f-a3d6-4a59-b95a-197dd01956b1/)

_Student_ has 2 attributes: _Name_ defined by String type, and _Age_
defined by int type. The class has 2 methods: _write()_ which
returns String type and _study()_ which returns nothing. Methods
also have brackets that can be filled in with some parameters. In
this example, we have the parameter _String_ str that is required to
activate method _write()_.

Each element of a class has a visibility option, defined before the 
name of the element. in this example, all the elements have a "+"
before their names. That means that all the visibility options of 
these elements are set to public. Let's elaborate on these visibility
options:
- (Public) + – elements can be accessed by any class in the
  system;
- (Private) - – elements can be accessed only by a class that
  owns it;
- (Protected) # – element can be accessed by classes that
  have a generalization (or inheritance) relationship with its
  class;
- (Package) ~ – element can be accessed by classes that are
  located in the same package.

####3. Description of class relationships
_Class relationships_ are a concept that defines connections
between classes. For example, we have 2 classes in our
applications: _Student headman_ and _Teacher_. We define their
connection by establishing a relationship of some sort. Here's an
example:

![](https://ucarecdn.com/0d7e90c4-8ad4-40c2-96a8-aa5c6a369af5/)

In this example, we use the type of relationship called
**generalization (or inheritance)**. Let's elaborate on the relationship
types.

- **Generalization (inheritance)** – a type of relationship where
  one class could be described as a child class which assumes
  and could use methods of a parent class. In our case _Student
  headman_ is the child class of _Teacher_. This relationship could
  be visualized by this arrow below:

![](https://ucarecdn.com/d3c4b587-4f62-4914-b58d-168e24fba828/)

- **Dependency** – a type of relationship that indicates that some
  change in one class can affect another class. Here's an
  example of _Student_ depending on School:

![](https://ucarecdn.com/5fae5232-59fe-4058-ba9d-865e11da5095/) 

- **Realization** – the relationship between the blueprint class
  and the object containing its respective implementation
  level details. For example, we have a class _Person_ which
  describes the basic attributes of a person. It's a blueprint
  that can be made into an object that represents a specific
  person like a _Student_, or a _Salesman_. Our _Student_ class can
  study and go to school, and our _Salesman_ class can go to
  work and sell stuff, but they are people, so they will have
  _Age_ and _Name_ attributes. Here's how you could visualize it:

![](https://ucarecdn.com/b98bd8df-9db7-490c-9283-a14f87355678/) 

####4. Description of association relationships
**Association** - a type of relationship that indicates that instances
of one class are connected to instances of another. For example,
_Teacher_ teaches _Student_. This relationship can be visualized by a 
straight line:

![](https://ucarecdn.com/5ee2f4d4-92c6-4c2f-b93c-965194c91271/)

Association relationships could also include a **cardinality** attribute.
Simply put, this attribute defines the number of instances of a 
class that could exist in this relationship. Here's how it can be
visualized for different situations:

![](https://ucarecdn.com/1f35163c-b76b-404f-b2cf-d6f7cd459e3a/)

A basic example of this concept is this: class _Teacher_ and class
_Student_ are connected by an association relationship. It means
that _Teacher_ teaches _Student_. One student can have one or 
multiple teachers, and the same can be said about teachers. So
the diagram that describes this relationship would look like this:

![](https://ucarecdn.com/f3eae881-ffd9-4d6a-add7-9451ed0426b9/)

Association relationships also have two special types:
- Aggregation - a special type of association relation that
  describes one class as a part of the other. Classes in this
  relation have a separate lifespan. If we come back to our
  _Student_ example, we can describe class _Student_ as part of a
  _Group_. This relation can be represented in this way:

![](https://ucarecdn.com/e876ec6f-8bef-4277-a367-1118233a49d2/)

- Composition - a special type of aggregation, where classes
  share lifespan. If the main class (_School_) stops its functions,
  the class that is a part of it (_Group_) will stop functioning too.
  This relationship can be visualized like this:

![](https://ucarecdn.com/0a45dc25-11ce-496e-99e9-3b062d09909c/)

####5. Conclusion
Class Diagram could be seen as too complicated at first. But when
you start working on your first project, making your first
framework, and connecting all the components into one structure,
you may realize that this way of presenting project structure is 
really helpful. It makes all the application components look more
apparent, and it also helps to set boundaries of their contents.
