# Seasons

# There's a file seasons.txt that looks like this:
# Spring
# Summer
# Autumn
# Winter

# We implemented the following code:
seasons_file = open('seasons.txt', 'r', encoding= 'utf8')

seasons = seasons_file.readlines()
favorite_seasons = seasons[2]
print(favorite_seasons)
seasons_file.close()