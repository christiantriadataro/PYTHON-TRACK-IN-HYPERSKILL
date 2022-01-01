# The daily_temp_c list contains average daily temperatures in New York in June.

# Convert these temperatures into the Fahrenheit scale. You can use function
# celsius_to_fahrenheit() defined below that converts a single observation from Celsius
# to Fahrenheit.

# How many days were there on which the temperature exceeded 80 degrees Fahrenheit?
# Print the answer on the screen.

def celsius_to_fahrenheit(c):
    return ((c + 40) * 1.8) - 40


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))
LIMIT = 80
temp_above_80 = list(filter(lambda x: x > LIMIT, daily_temp_f))

print(len(temp_above_80))