# Personal assistant
# You are trying to write a personal assistant, and one of its tasks is
# to print the local time for a user. Write a piece of code that would
# do that using the strftime() function with the output format:
# "It's 09:11."

import time

# put your python code here
current = time.strftime("%H:%M", time.localtime())
print(f"It's {current}")
time.asctime()
time.time()