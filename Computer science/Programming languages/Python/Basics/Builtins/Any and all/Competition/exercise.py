# Today you are taking part in the chess competition. The winner
# of the competition will get the "winner" status and the largest
# amount of money if they win all the games. Much is at stake!

# The results are stored in a list. Fill in the blanks in the code below
# and figure out how much money you won.

# You DON'T need to print the answer.

check = all([True, True, 1, 1, True])

if check:
    status = 'winner'
else:
    status = 'loser'

if status == 'winner':
    winning_sum = 100
else:
    winning_sum = 10

print(winning_sum)