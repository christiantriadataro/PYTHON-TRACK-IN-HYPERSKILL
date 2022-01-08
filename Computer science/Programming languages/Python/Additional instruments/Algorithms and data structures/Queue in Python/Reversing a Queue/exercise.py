# We created a deque my_queue and appended some elements to it, using appendleft()
# (so the head of the queue is on the right). Your task is to create the queue
# reversed_queue that would contain the elements of my_queue in the reversed order.

# For example, if my_queue contain elements 1, 2, and 3, then reversed_queue should
# contain elements 3, 2, 1.

# You don't need to print out the resulting queue.
from collections import deque
my_queue = deque()
my_queue.append("Left")
my_queue.append("Middle")
my_queue.append("Right")
print(my_queue)
my_queue.reverse()

print(my_queue)

reversed_queue = deque(reversed(my_queue))