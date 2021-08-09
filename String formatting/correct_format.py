# Which of the following examples will correctly output formatted
# strings?

# If a code snippet raises SyntaxError or formatting doesn't
# actually take place in a string, consider such an option
# incorrect.

print("%.4f".format(3.14159265358979))
# %.4f
print("{1} {1} {1}".format(1, 2, 3))
# 2 2 2
print("{1} is a {kind}".format(kind="fruit", "grapefruit"))
# SyntaxError 
print("{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon"))
# Lisbon is the capital of Portugal 