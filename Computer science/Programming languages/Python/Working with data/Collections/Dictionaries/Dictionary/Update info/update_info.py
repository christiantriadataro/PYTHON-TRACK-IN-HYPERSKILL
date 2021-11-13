# Let's say you have a dict with children's names and professions
# they would like to have when they grow up:
children = {'Emily': 'artist', 'Adam': 'astronaut', 
            'Nancy': 'programmer'}
# But what if someone's choice has changed? Say, Emily now
# wants to be a musician. Update the dict and print the new
# version.

children['Emily'] = 'musician'
print(children)