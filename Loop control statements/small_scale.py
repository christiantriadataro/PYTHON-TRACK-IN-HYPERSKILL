# Read lines with floats from the input until you get a single
# period . that signals you to stop.

# Find the minimum of these numbers and print it out.

numbers = []
while True:
    number = input()
    if number == '.':
        break
    numbers.append(float(number))
print(min(numbers))