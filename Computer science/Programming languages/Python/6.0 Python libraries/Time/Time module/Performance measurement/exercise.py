# Performance measurement

# Complete the piece of code to find out the time it took to execute
# the program.

import time

start = time.perf_counter()
end = time.perf_counter()

total_time = end - start

print(f"The program has executed for {total_time} seconds.")
