## Theory: Deque

#### 1. Essentials
**Deque** is a generalization of the queue that allows elements to 
be inserted and removed from both ends of it. The term deque
comes from "double-ended queue". Deques combine access
rules provided by queues (FIFO) and stacks (LIFO).

The following picture demonstrates a deque with seven
elements:

![](https://ucarecdn.com/365a00f4-6158-431c-97f7-a36c8b2bc813/)

#### 2. Operations
There are four basic operations on it:
- insert an element at the front;
- insert an element at the back;
- remove an element from the front;
- remove an element from the back.

Suppose we execute the following operations on the deque
presented above:

    remove an element from the front
    remove an element from the front
    remove an element from the front
    insert 20 to the front
    remove an element from the back
    remove an element from the back
    insert 30 to the back

The result is shown below:

![](https://ucarecdn.com/73ac1f36-6786-4113-9139-ee5899941751/)

A deque often has some additional operations that allows us to
see the first and the last elements without removing them
(examine the front and examine the back) as well as obtaining 
the number of the elements in it. Usually, deques does not support
indexing, but some implementations may provide it.

#### 3. Application
Developers use deques less often than regular queues. The
most common example of deques are:
- **undo-redo** operations in software like graphic editors or 
  IDEs;
- **steal task scheduling algorithms**: a processor takes the
  first task from its deque and performs it; when on of the 
  processors completes execution of its own tasks, it steals
  the last task from the deque of another processor and 
  executes it.

Yet, of course, there are still many other cases where deques
can help you.