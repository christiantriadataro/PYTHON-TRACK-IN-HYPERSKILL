# Several warm-up matches have been played at the tennis tournament. You have data pm
# the victories and losses of some players. Save the names of the winners to a list and
# calculate the total number of victories.

# The input format;
# On the first line, you'll receive the integer n specifying a number of lines.

# The next n lines will look either Name win or Name loss.

# The output format:
# On the first line, print out the list of all players that have won a match, repeat the names
# if necessary.

# Then output the total number of victories based on your list.
winners = [winners.replace(' win', '') for winners in [input() for _ in range(int(input()))] if 'win' in winners]
print(winners)
print(len(winners))
# print([winners.strip(' win') for winners in [input() for _ in range(int(input()))] if 'win' in winners])