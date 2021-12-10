# --String formatting--

print(11 / 3)  # 3.6666666666666665
print('%.3f' % (11/3))  # 3.667
print('%.2f' % (11/3))  # 3.67


# --str.format() method--

print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
# Mix 2 eggs, 30 g of milk and a pinch of salt to make an ideal omelet.

print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# Strangers in the Night by Frank Sinatra
print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
# Night in the Strangers by Frank Sinatra

print('The {film} at {theatre} was {adjective}!'.format(film = 'Lord of the Rings', adjective = 'incredible', theatre = 'BFI Max'))
# The Lord of the Rings at BFI IMAX was incredible!

print('The {0} was {adjective}'.format('Lord of the Rings', adjective = 'incredible'))
# The Lord of the Rings was incredible!

print('The {0} was {adjective}!'.format('Lord of the Rings', adjective = 'incredible'))
# SyntaxError: positional argument follows keyword argument


# --Formatted string literals--

name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
print(f'{name}, the {title}, is {reign}.')
# Elizabeth II, the Queen of the United Kingdom and the other Commonwealth realms, is the longest-lived and longest-reigning British monarch.

hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7