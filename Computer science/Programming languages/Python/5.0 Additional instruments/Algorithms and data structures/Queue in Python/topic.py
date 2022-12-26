# Theory: Queue in Python

# 1. Queue
# Queue is a linear data structure that implements the first-
# in-first-out (FIFO) principle, meaning that new elements
# can be added to the back of the queue, while removing an
# element is only possible from its head. Queue is really
# just like any real-life line in a supermarket: customers
# who come first are attended first, while the others are
# waiting for their turn.

# Typically queue supports the following two basic
# operations:
# - enqueue, that adds a new element to the back of the
#   queue.
# - dequeue, that removes the first element of the queue.

# Sometimes, operations front and rear are also supported.
# They return the first and the last element of the queue
# respectively without removing them.

# In practice, queues are especially useful in threaded
# programming when information must be exchanged
# between multiple threads. Queues are at the heart of job
# schedulers, helping to schedule delayed tasks efficiently
# while preserving the order in which they must be
# performed.

# In this topic, you will get familiar with a data structure
# called queue and how to implement it in Python.

# 2. Deque
# Before we learn how to implement queue in Python, we
# should get familiar with one more data structure that is
# closely related, namely deque. Deque stands for 'double-
# ended queue' and alows for the elements to be added
# and removed from either side.

# In Python, you can find deque implementation in the
# collections module. The essential methods are
# append(element) and appendleft(element), which add a
# new element to the right or left side of the deque
# respectively, as well as pop() and popleft(), which
# remove the first element from the corresponding side of
# the deque.

# Let's take a look at the example:

from collections import deque

my_deque = deque()

my_deque.append('Middle')
my_deque.append('Right')

my_deque.appendleft('Left')

print(my_deque)

# deque(['Left', 'Middle', 'Right'])

print(my_deque.pop())

# Right

print(my_deque)

# deque(['Left', 'Middle'])

print(my_deque.popleft())

# Left

print(my_deque)

# deque(['Middle'])

# Deq