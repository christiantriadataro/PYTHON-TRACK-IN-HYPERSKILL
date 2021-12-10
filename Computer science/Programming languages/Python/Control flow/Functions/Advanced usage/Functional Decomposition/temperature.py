# Below you can see a draft of a program for a basic temperature
# converter from Fahrenheit to Celsius and vice versa. You need to
# finish the program by creating a sort of entry point for the 
# program in the function main.

# In this function, you should:
# - process the input. The input is a string containing a
#   temperature value and a unit of measurement which are
#   seperated by a whitespace character. We already wrote the
#   code that reads the input and creates the variables, but you
#   still need to figure out what the right type is for each of
#   them and convert if necessary;
# - call the appropriate function depending on what was given
#   in the input;
# - print the converted temperature with the new unit.

# Use the examples as a guide.

# You do NOT need to call the function main.

def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)

def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)

def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    if unit == "F":
        print(fahrenheit_to_celsius(float(temperature)), "C")
    else:
        print(celsius_to_fahrenheit(float(temperature)), "F")
main()


