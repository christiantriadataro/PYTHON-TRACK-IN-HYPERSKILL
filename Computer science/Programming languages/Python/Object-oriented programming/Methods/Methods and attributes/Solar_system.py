# Create a file planets.txt and write the names of the Solar system
# planets there, each on a new line. In total, the file should
# contain 8 lines with the following planets: Mercury, Venus,
# Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.

# When opening the file, specify encoding='utf-8'.

# create the planets.txt
_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Uranus', 'Neptune']
with open('planets.txt', 'w', encoding='utf-8') as file:
    [file.write(x + '\n') for x in _planets]
    pass
